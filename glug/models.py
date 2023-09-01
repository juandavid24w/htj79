from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4

# Create your models here.


class GLUG(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid4,
                          editable=False,
                          verbose_name='id')
    name = models.CharField(max_length=256,
                            verbose_name=_('GLUG Name'),
                            help_text=_('Enter your GLUG name.'))
    institute = models.ForeignKey(
        'institutions.Institutions',
        on_delete=models.RESTRICT,
        verbose_name=_('Institute'),
        help_text=('Pick your Institute you are associated with.'))
    location = models.ForeignKey('hacktivist.Locations',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Location'),
                                 help_text=_('Pick your GLUG location.'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      auto_created=True,
                                      null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} | {self.location.district}'

    class Meta:
        ordering = ['name', '-updated_at']
        verbose_name = 'GNU/Linux Users Group'
        verbose_name_plural = 'GNU/Linux Users Group'
