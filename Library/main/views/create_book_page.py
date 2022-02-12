from django.shortcuts import render, redirect
from django.views import View

from Library.main.forms.create_book import CreateBookForm
from Library.main.models import Book, Profile


class CreateBookView(View):
    def get(self, req):
        form = CreateBookForm()
        return render(req, "add-book.html", {
            "form": form,
        })

    def post(self, req):
        form = CreateBookForm(req.POST, instance=Book(user_profile=Profile.objects.first()))
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(req, "add-book.html", {
            "form": form
        })
