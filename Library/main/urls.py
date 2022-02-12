from django.urls import path

from Library.main.views.create_book_page import CreateBookView
from Library.main.views.delete_book import DeleteBookView
from Library.main.views.delete_profile import DeleteProfileView
from Library.main.views.details_page import DetailsView
from Library.main.views.edit_book_page import EditBookView
from Library.main.views.edit_profile_page import EditProfileView
from Library.main.views.home_page import HomeView
from Library.main.views.profile_page import ProfileDetails

urlpatterns = [
    path("", HomeView.as_view(), name="home-page"),
    path("add", CreateBookView.as_view(), name="add-page"),
    path("edit/<int:pk>", EditBookView.as_view(), name="edit-page"),
    path("details/<int:pk>", DetailsView.as_view(), name="details-page"),
    path("delete/<int:pk>", DeleteBookView.as_view(), name="delete-page"),
    path("profile", ProfileDetails.as_view(), name="profile-page"),
    path("profile/edit", EditProfileView.as_view(), name="profile-edit-page"),
    path("profile/delete", DeleteProfileView.as_view(), name="profile-delete-page"),
]
