from PIL import Image as PILImage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from .models import Image
from .forms import ImageForm


class HistoryView(LoginRequiredMixin, ListView):
    """View for displaying the user's image history."""

    model = Image
    template_name = "img_resizer/history.html"
    context_object_name = "images"

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)


class ResizeView(LoginRequiredMixin, CreateView):
    """View for resizing an image.
    The form is submitted to this view, and the image is resized and saved.
    the resizing is done using the PIL library.
    https://cloudinary.com/guides/bulk-image-resize/python-image-resize-with-pillow-and-opencv
    """

    model = Image
    form_class = ImageForm
    template_name = "img_resizer/resize.html"

    def form_valid(self, form):
        """
        1. Set the user of the image to the current user.
        2. Save the image to the database.
        3. Open the image using PIL.
        4. Resize the image.
        5. Save the resized image.
        """

        form.instance.user = self.request.user
        self.object = form.save(commit=False)
        self.object.save()
        original_image = PILImage.open(self.object.image)
        resized_image = original_image.resize(
            (self.object.new_width, self.object.new_height)
        )
        resized_image.save(self.object.image.path)
        return super().form_valid(form)

    def get_success_url(self):
        return f"/download/{self.object.pk}/"


class DownloadView(LoginRequiredMixin, DetailView):
    """View for downloading an image."""

    model = Image
    template_name = "img_resizer/download.html"
    context_object_name = "image"

    def get_object(self):
        return Image.objects.get(pk=self.kwargs["pk"], user=self.request.user)
