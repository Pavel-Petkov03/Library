from django.shortcuts import render, redirect
from django.views import View

from Library.main.forms.create_profile import CreateProfileForm
from Library.main.models import Book
from Library.main.utils import check_if_has_profile


class HomeView(View):
    def get(self, req):
        if check_if_has_profile():
            books = Book.objects.all()
            return render(req, "home-with-profile.html", {
                "books": books
            })
        form = CreateProfileForm()
        return render(req, "home-no-profile.html", {
            "form": form
        })

    def post(self, req):
        form = CreateProfileForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(req, "home-no-profile.html", {
            "form": form
        })
