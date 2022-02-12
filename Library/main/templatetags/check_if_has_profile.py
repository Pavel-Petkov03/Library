from django import template

from Library.main.models import Profile

register = template.Library()


@register.simple_tag
def check_if_has_profile():
    return Profile.objects.first()
