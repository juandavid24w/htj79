from django.db import models
from hacktivist.models import Platform
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _
from django.conf import settings
import uuid
from django.utils.text import slugify
from PIL import Image


# Create your models here.
class Meetups(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    title = models.TextField()
    slug = models.SlugField(unique=True, null=False, blank=True)
    location = models.ForeignKey("hacktivist.Locations", on_delete=models.CASCADE)
    glug = models.ForeignKey("glug.GLUG", on_delete=models.RESTRICT)
    date = models.DateField()
    time = models.TimeField()
    mode = models.CharField(choices=Platform.choices)
    venue = models.TextField()
    description = models.TextField()
    poster = models.ImageField(
        verbose_name=_("Poster"), upload_to="meetups/poster/", null=True
    )
    minutes = models.FileField(validators=[FileExtensionValidator(["pdf"])], null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        # Poster need to be saved in permanent location for PIL to resize
        img = Image.open(self.poster.path)
        if img.height > 1080 or img.width > 1080:
            output_size = (1080, 1080)
            img.thumbnail(output_size)
            img.save(self.poster.path)

    def __str__(self):
        return f"{self.glug} ({self.location})"

    class Meta:
        ordering = ["-date", "-time"]
