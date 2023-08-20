from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from hacktivist.models import Gender, BloodGroup, Occupation, EducationalQualification

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
    contact_full = models.CharField(max_length=15, null=True, blank=True)
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
    profile_status = models.CharField(max_length=50,
                                      verbose_name=_('Profile Status'),
                                      choices=PROFILE_STATUS_CHOICES,
                                      default=1)
    is_accept_TC = models.BooleanField(verbose_name=_('Terms & Conditions'),
                                       default=False)
    is_news_subscribed = models.BooleanField(
        verbose_name=_('Hacktivist News updates'), default=False)

    def save(self, *args, **kwargs):
        if len(self.contact) == 10 and self.contact.isnumeric():
            self.contact_full = f'{self.zip_code}{self.contact}'
            super(Members, self).save(*args, **kwargs)
        else:
            raise ValidationError('Invalid Contact Details')

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
    verified_by = models.ForeignKey('member.Members',
                                    on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True,
                                      auto_created=True,
                                      null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.is_verified} | {self.verified_by.username}'

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
    year = models.DateField(auto_now_add=True, auto_created=True)
    member = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.RESTRICT)
    join_date = models.DateField()
    start_date = models.DateField(auto_now_add=True, auto_created=True)
    payment_method = models.CharField(max_length=30,
                                      choices=PAYMENT_METHOD_CHOICES)
    payment_received = models.IntegerField()
    payment_pending = models.IntegerField()
    proof_of_payment = models.ForeignKey('member.ProofOfPayment',
                                         on_delete=models.RESTRICT)
    status = models.BooleanField(choices=MEMBERSHIP_STATUS_CHOICES)
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
