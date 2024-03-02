from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Image(models.Model):
    """
    Represents an uploaded and resized image.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    original_width = models.PositiveIntegerField()
    original_height = models.PositiveIntegerField()
    new_width = models.PositiveIntegerField()
    new_height = models.PositiveIntegerField()

    def __str__(self):
        return self.image.name
