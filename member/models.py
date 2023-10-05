from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from hacktivist.models import Gender, BloodGroup, Occupation, EducationalQualification
from datetime import date

# Create your models here.


class Members(AbstractUser, PermissionsMixin):
    PROFILE_STATUS_CHOICES = (
        (1, 'Profile Info'),
        (2, 'Membership'),
        (3, 'Payment Proof'),
        (4, 'Proof Confirmation'),
        (5, 'Success'),
    )
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    dob = models.DateField(verbose_name=_('Date of Birth'),
                           blank=True,
                           null=True)
    gender = models.CharField(max_length=10,
                              choices=Gender.choices,
                              verbose_name=_('Gender'),
                              blank=True)
    glug = models.ForeignKey('glug.GLUG',
                             on_delete=models.RESTRICT,
                             verbose_name='GLUG',
                             blank=True,
                             null=True)
    institute = models.ForeignKey('institutions.Institutions',
                                  on_delete=models.RESTRICT,
                                  verbose_name=_('Institution'),
                                  blank=True,
                                  null=True)
    country_code = models.CharField(max_length=5, default='+91')
    contact = models.CharField(max_length=10, verbose_name=_('Contact'))
    blood_group = models.CharField(max_length=10,
                                   choices=BloodGroup.choices,
                                   blank=True)
    address = models.TextField(verbose_name=_('Address'), blank=True)
    display_pic = models.ImageField(verbose_name=_('Profile picture'),
                                    default="defaults/user.png",
                                    upload_to="users/display_pics/")
    occupation = models.CharField(max_length=30,
                                  choices=Occupation.choices,
                                  blank=True)
    edu_qualification = models.CharField(
        max_length=30, choices=EducationalQualification.choices, blank=True)
    stream = models.CharField(max_length=256, blank=True)
    profile_status = models.IntegerField(verbose_name=_('Profile Status'),
                                         choices=PROFILE_STATUS_CHOICES,
                                         default=1)
    is_accept_TC = models.BooleanField(verbose_name=_('Terms & Conditions'),
                                       default=False)
    is_news_subscribed = models.BooleanField(
        verbose_name=_('Hacktivist News updates'), default=False)

    @property
    def contact_full(self):
        return f'{self.country_code}{self.contact}'

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.username}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique email')
        ]
        ordering = ['-date_joined', 'first_name', 'username']
        verbose_name = _('Member')
        verbose_name_plural = _('Members')


class ProofOfPayment(models.Model):
    VERIFY_CHOICES = (
        (0, 'Not Verified'),
        (1, 'Verified'),
    )
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    transaction_id = models.BigIntegerField()
    document = models.FileField(
        upload_to='users/payments/%Y/%m/%d/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])
        ])
    is_verified = models.BooleanField(choices=VERIFY_CHOICES, default=0)
    verified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True,
                                      auto_created=True,
                                      null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.transaction_id} | {self.verified_by.username}'

    class Meta:
        ordering = ['-updated_at']
        verbose_name = _('Proof of payment')
        verbose_name_plural = _('Proof of Payments')


class Membership(models.Model):
    MEMBERSHIP_STATUS_CHOICES = (
        (0, 'Expried/Invalid'),
        (1, 'Valid'),
    )
    PAYMENT_METHOD_CHOICES = (
        ('cash', 'Cash'),
        ('upi', 'UPI Payment'),
        ('bank', 'Net Banking'),
    )
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    year = models.IntegerField(default=date.today().year,
                               verbose_name=_('Year of Join'))
    member = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.RESTRICT)
    join_date = models.DateField(auto_now_add=True, auto_created=True)
    start_date = models.DateField(auto_now_add=True, auto_created=True)
    payment_method = models.CharField(max_length=30,
                                      choices=PAYMENT_METHOD_CHOICES)
    payment_received = models.IntegerField()
    payment_pending = models.IntegerField(default=0)
    proof_of_payment = models.ForeignKey('member.ProofOfPayment',
                                         null=True,
                                         blank=True,
                                         on_delete=models.RESTRICT)
    status = models.BooleanField(choices=MEMBERSHIP_STATUS_CHOICES,
                                 verbose_name=_('Status'),
                                 null=True,
                                 blank=True)
    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True,
                                      auto_created=True,
                                      null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.member.first_name} {self.member.last_name} | {self.member.username}'

    class Meta:
        ordering = ['-year', 'member']
        verbose_name = _('Membership')
        verbose_name_plural = _('Memberships')
