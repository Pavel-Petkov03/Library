from django.shortcuts import render, redirect
from django.views import View

from Library.main.models import Book


class DetailsView(View):
    def get(self, req, pk):
        return render(req, "book-details.html", {
            "book": Book.objects.get(id=pk)
        })


