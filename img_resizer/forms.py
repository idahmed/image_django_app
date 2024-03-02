from .models import Image
from django import forms


class ImageForm(forms.ModelForm):
    """image upload form."""

    class Meta:
        model = Image
        fields = [
            "name",
            "image",
            "original_width",
            "original_height",
            "new_width",
            "new_height",
        ]

        ## widgets are used to define the html input element
        ## https://docs.djangoproject.com/en/5.0/ref/forms/widgets/#widget
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "original_width": forms.NumberInput(
                attrs={"readonly": "readonly", "class": "form-control"}
            ),
            "original_height": forms.NumberInput(
                attrs={"readonly": "readonly", "class": "form-control"}
            ),
            "new_width": forms.TextInput(attrs={"class": "form-control"}),
            "new_height": forms.TextInput(attrs={"class": "form-control"}),
        }
