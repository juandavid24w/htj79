from factory.django import DjangoModelFactory, FileField
from factory import SubFactory
from datetime import date
from django.conf import settings
from member.models import ProofOfPayment, Membership
from software.models import Tag, Category, License, Software


# Create your factories here.
class MemberFactory(DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    username = "demo_user"
    password = "demo_pass"
    is_superuser = True
    is_staff = True


class ProofOfPaymentFactory(DjangoModelFactory):
    class Meta:
        model = ProofOfPayment

    transaction_id = "1234567890"
    document = FileField
    verified_by = SubFactory(MemberFactory)


class MembershipFactory(DjangoModelFactory):
    class Meta:
        model = Membership

    member = SubFactory(MemberFactory)
    payment_method = "cash"
    payment_received = 50
    proof_of_payment = SubFactory(ProofOfPaymentFactory)
    expiry_date = date.today()

class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag
    
    