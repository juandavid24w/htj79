from django.db import models
from hacktivist.models import Platform
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.conf import settings
from hacktivist.models import Locations
from glug.models import GLUG


# Create your models here.
class Meetups(models.Model):
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.ForeignKey("hacktivist.Locations", on_delete=models.CASCADE)
    glug = models.ForeignKey("glug.GLUG", on_delete=models.RESTRICT)
    date = models.DateField()
    time = models.TimeField()
    mode = models.CharField(choices=Platform.choices)
    venue = models.TextField()
    description = models.TextField()
    poster = models.ImageField(verbose_name=_("Poster"), upload_to="meetups/poster/")
    minutes = models.FileField(validators=[FileExtensionValidator(["pdf"])])

    def __str__(self):
        return f"{self.glug} ({self.location})"
