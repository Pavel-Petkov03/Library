from django.shortcuts import render, redirect
from django.views import View

from Library.main.forms.create_book import CreateBookForm
from Library.main.models import Book


class EditBookView(View):
    def get(self, req, pk):
        current_book = Book.objects.get(id=pk)
        return render(req, "edit-book.html", {
            "form": CreateBookForm(instance=current_book),
            "book": current_book
        })

    def post(self, req, pk):
        form = CreateBookForm(req.POST, instance=Book.objects.get(id=pk))
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(req, "edit-book.html", {
            "form": form
        })
