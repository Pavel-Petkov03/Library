from django.shortcuts import render, redirect
from django.views import View

from Library.main.forms.delete_profile import DeleteProfileForm
from Library.main.models import Profile, Book


class DeleteProfileView(View):
    def get(self, req):
        form = DeleteProfileForm(instance=Profile.objects.first())
        return render(req, "delete-profile.html", {
            "form": form
        })

    def post(self, req):
        Profile.objects.first().delete()
        return redirect("/")
