from Library.main.models import Profile


def check_if_has_profile():
    return Profile.objects.exists()
