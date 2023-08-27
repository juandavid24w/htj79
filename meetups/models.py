from django.db import models
from hacktivist.models import Platform
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _


# Create your models here.
class Meetups(models.Model):
    location = models.ForeignKey('hacktivist.Locations', on_delete= models.CASCADE)
    glug = models.ForeignKey('glug.GLUG', on_delete=models.RESTRICT)
    date = models.DateField()
    time = models.TimeField()
    platform = models.CharField(choices=Platform.choices)
    venue = models.TextField()
    description = models.TextField()
    minutes = models.FileField(
        upload_to='meetups/minutes/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf'])
        ])
    poster = models.ImageField(verbose_name=_('Poster'),
                                    upload_to="meetups/poster/")

    def __str__(self):
        return f'{self.glug} ({self.location})'
    