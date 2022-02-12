from Library.main.forms.create_profile import CreateProfileForm


class DeleteProfileForm(CreateProfileForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()

    def disable_fields(self):
        for (name, field) in self.fields.items():
            field.widget.attrs["disabled"] = True
