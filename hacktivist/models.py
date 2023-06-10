from django.contrib.gis.db import models
from django.contrib.gis.geos import point
from django.utils.translation import gettext as _


class Locations(models.Model):
    district = models.CharField(max_length=256,
                                verbose_name=_('district'),
                                help_text=_(''))
    state = models.CharField(max_length=256,
                             verbose_name=_('state'),
                             help_text=_(''))
    country = models.CharField(max_length=256,
                               verbose_name=_('country'),
                               help_text=_(''),
                               default='India')
    location = models.PointField(geography=True,
                                 verbose_name=_('location'),
                                 help_text=_('point your GLUG location'),
                                 null=True,
                                 blank=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      auto_created=True,
                                      null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.district}'

    class Meta:
        verbose_name = _('location')
        verbose_name_plural = _('locations')


class Gender(models.TextChoices):
    man = 'Man'
    woman = 'Woman'
    trans = 'Trans'
    queer = 'Queer'
    other = 'Other'


class BloodGroup(models.TextChoices):
    op = 'O+ve'
    on = 'O-ve'
    ap = 'A+ve'
    an = 'A-ve'
    bp = 'B+ve'
    bn = 'B-ve'
    abp = 'AB+ve'
    abn = 'AB-ve'


class Occupation(models.TextChoices):
    s_student = 'School Student'
    c_student = 'College/University Student'
    researcher = 'Researcher'
    it_employee = 'IT Employee'
    ites_employee = 'ITES Employee'
    non_it_ites_employee = 'Non IT/ITES Employee'
    self_employed = 'Self Employed'
    unemployed = 'Unemployed'


class EducationalQualification(models.TextChoices):
    eighth_pass = '8th Pass'
    tenth_pass = '10th Pass'
    twelveth_pass = '12th Pass'
    diploma = 'Diploma'
    under_graduate = 'Under Graduate'
    post_graduate = 'Post Graduate'
    doctorate = 'Doctorate'