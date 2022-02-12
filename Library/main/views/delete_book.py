from django.shortcuts import redirect
from django.views import View

from Library.main.models import Book


class DeleteBookView(View):
    def get(self, req, pk):
        Book.objects.get(id=pk).delete()
        return redirect("/")
