from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        ordering = ["name"]
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        ordering = ["name"]
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class License(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    url_source = models.URLField(verbose_name=_("License URL"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        ordering = ["name"]
        verbose_name = _("License")
        verbose_name_plural = _("Licenses")


class Software(models.Model):
    CHOICES_IS_FOSS = (
        (True, "Is FOSS"),
        (False, "Is not FOSS"),
    )

    name = models.CharField(
        max_length=50, verbose_name=_("Name"), help_text=_("Software name")
    )
    url_wikipedia = models.URLField(
        verbose_name=_("Wikipedia URL"), null=True, blank=True
    )
    page_home = models.URLField(verbose_name=_("Homepage"), null=True, blank=True)
    tags = models.ManyToManyField("software.Tag", verbose_name=_("Tags"))
    category = models.ManyToManyField("software.Category", verbose_name=_("Categories"))
    alternatives = models.ManyToManyField(
        "software.Software",
        verbose_name=_("Alternative Softwares"),
        blank=True,
    )
    is_foss = models.BooleanField(
        choices=CHOICES_IS_FOSS, verbose_name=_("is FOSS"), null=True, blank=True
    )
    license = models.ForeignKey(
        "software.License", on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} | {self.is_foss}"

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = _("Software")
        verbose_name_plural = _("Softwares")
