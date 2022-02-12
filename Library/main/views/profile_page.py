from django.shortcuts import render
from django.views import View

from Library.main.models import Profile


class ProfileDetails(View):
    def get(self, req):
        return render(req, "profile.html", {
            "user": Profile.objects.first()
        })
