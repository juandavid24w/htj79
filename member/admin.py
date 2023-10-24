from django.contrib import admin
from member.models import Membership, ProofOfPayment, Members

# Register your models here.


class MembershipAdmin(admin.ModelAdmin):
    list_display = [
        "member",
        "join_date",
        "expiry_date",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]


class ProofOfPaymentAdmin(admin.ModelAdmin):
    list_display = [
        "transaction_id",
        "is_verified",
    ]
    readonly_fields = [
        "transaction_id",
        "document",
        "is_verified",
        "verified_by",
        "created_at",
        "updated_at",
    ]


class MembersAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProofOfPayment, ProofOfPaymentAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Members, MembersAdmin)
