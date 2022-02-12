from django.shortcuts import render, redirect
from django.views import View

from Library.main.forms.create_profile import CreateProfileForm
from Library.main.models import Profile


class EditProfileView(View):
    def get(self, req):
        return render(req, "edit-book.html", {
            "form": CreateProfileForm(instance=Profile.objects.first())
        })

    def post(self, req):
        form = CreateProfileForm(req.POST, instance=Profile.objects.first())
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(req, "edit-book.html", {
            "form": form
        })
