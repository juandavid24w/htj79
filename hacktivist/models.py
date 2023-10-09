from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _
from uuid import uuid4


class Locations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    district = models.CharField(
        max_length=256,
        verbose_name=_("district"),
    )
    state = models.CharField(max_length=256, verbose_name=_("state"))
    country = models.CharField(
        max_length=256,
        verbose_name=_("country"),
        default="India",
    )
    location = models.PointField(
        geography=True,
        verbose_name=_("location"),
        help_text=_("point your Institution/GLUG location"),
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def longitude(self):
        if self.location == None:
            return None
        else:
            return self.location.x

    @property
    def latitude(self):
        if self.location == None:
            return None
        else:
            return self.location.y

    def __str__(self):
        return f"{self.district}"

    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")


# Text Choices
class Gender(models.TextChoices):
    man = "Man", "Man"
    woman = "Woman", "Woman"
    trans = "Trans", "Trans"
    queer = "Queer", "Queer"
    other = "Other", "Other"


class BloodGroup(models.TextChoices):
    op = "O+ve", "O+ve"
    on = "O-ve", "O-ve"
    ap = "A+ve", "A+ve"
    an = "A-ve", "A-ve"
    bp = "B+ve", "B+ve"
    bn = "B-ve", "B-ve"
    abp = "AB+ve", "AB+ve"
    abn = "AB-ve", "AB-ve"


class Occupation(models.TextChoices):
    student_school = "School Student", "School Student"
    student_college = "College/University Student", "College/University Student"
    researcher = "Researcher", "Researcher"
    employee_it = "IT Employee", "IT Employee"
    employee_ites = "ITES Employee", "ITES Employee"
    employee_others = "Non IT/ITES Employee", "Non IT/ITES Employee"
    employee_self = "Self Employed", "Self Employed"
    unemployed = "Unemployed", "Unemployed"


class EducationalQualification(models.TextChoices):
    eighth_pass = "8th Pass", "8th Pass"
    tenth_pass = "10th Pass", "10th Pass"
    twelfth_pass = "12th Pass", "12th Pass"
    diploma = "Diploma", "Diploma"
    under_graduate = "Under Graduate", "Under Graduate"
    post_graduate = "Post Graduate", "Post Graduate"
    doctorate = "Doctorate", "Doctorate"


class Platform(models.TextChoices):
    online = "Online", "Online"
    offline = "Offine", "Offline"


class Subscription(models.Model):
    name = models.CharField(
        max_length=256, verbose_name=_("name"), help_text=_("Subscription name")
    )
    validity = models.IntegerField(
        verbose_name=_("Validity"),
        help_text=_("Validity of subscription in years"),
        default=1,
    )
    occupation = ArrayField(
        models.CharField(max_length=256, choices=Occupation.choices),
        size=10,
        verbose_name=_("Occupation"),
        blank=True,
        null=True,
    )
    price = models.IntegerField(
        verbose_name=_("Price"), help_text=_("Price for the subscriptions")
    )
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} | {self.price}"

    class Meta:
        verbose_name = _("subscription")
        verbose_name_plural = _("subscriptions")
