from pytest_factoryboy import register
from factoryConf.factories import (
    MemberFactory,
    ProofOfPaymentFactory,
    MembershipFactory,
)

"""
All factory registered will be accessed by its snake casing in your test file
Eg:
DemoFactory -> demo_factory
"""

# Member module
register(MemberFactory)  # member_factory
register(ProofOfPaymentFactory)  # proof_of_payment_factory
register(MembershipFactory)  # membership_factory

# Software module
