from django.shortcuts import render, redirect
from django.views import View


def allowed_add_context_decorator(array_of_allowed_funcs=[]):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if func.__name__ in array_of_allowed_funcs:
                return func(*args, **kwargs)
            else:
                func.__self__.add_context = lambda request: {}

        return wrapper

    return decorator


class CustomView(View):
    """
    This class must be used only if you want to use forms with the pattern expressed bellow
    there is no use of using this class without forms or overwriting get and post functions
    """
    failure_redirect_url = ""
    template = ""
    model = None
    form = None
    allowed_add_context_functions = []

    def query(self, pk):
        return self.model.objects.get(pk=pk)

    @allowed_add_context_decorator(allowed_add_context_functions)
    def get(self, request, pk=None):
        if pk:
            custom_form = self.form(instance=self.query(pk))
        else:
            custom_form = self.form()
        return render(request, self.template, {
            "form": custom_form
        })

    @allowed_add_context_decorator(allowed_add_context_functions)
    def post(self, request, pk=None):
        if pk:
            custom_form = self.form(request.POST, request.FILES, instance=self.model.objects.get(pk=pk))
        else:
            custom_form = self.form(request.POST, request.FILES)
        if custom_form.is_valid():
            self.perform_action(request, custom_form)
            return redirect(self.failure_redirect_url)

        return render(request, self.template, context)

    def perform_action(self, request, form):
        """
        This function could be overridden when you want to make actions with the model which can be taken from the class or pass
        another one directly and use request to take params from it
        """
        form.save()

    def add_context(self, request):
        return {}
