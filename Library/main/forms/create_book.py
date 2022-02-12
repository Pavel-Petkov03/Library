from django import forms

from Library.main.models import Book


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "description", "image", "type"]

        widgets = {
            "title": forms.TextInput(attrs={
                "type": "text", "name": "title", "maxlength": 30, "required": "", "id": "title",
                "placeholer": "Title"
            }),
            "description": forms.Textarea(attrs={
                "name": "description", "rows": "100", "cols": "40", "required": "", "id": "description",
                "placeholer": "Description"
            }),

            "image": forms.URLInput(attrs={
                "type": "url", "name": "image", "maxlength": 200, "required": "", "id": "image",
                "placeholer": "Image"
            }),
            "type": forms.TextInput(attrs={
                "type": "text", "name": "type", "maxlength": 30, "required": "", "id": "type",
                "placeholer": "Fiction, Novel, Crime.."
            }),
        }

        labels = {
            "title": "Title",
            "description": "Description",
            "image": "Image",
            "type": "Type"
        }
