from django.contrib import admin
from member.models import Membership, ProofOfPayment

# Register your models here.


class MembershipAdmin(admin.ModelAdmin):
    list_display = [
        'member',
        'join_date',
        'expiry_date',
    ]
    readonly_fields = [
        'created_at',
        'updated_at',
    ]


class ProofOfPaymentAdmin(admin.ModelAdmin):
    list_display = [
        'transaction_id',
        'is_verified',
    ]
    readonly_fields = [
        'transaction_id',
        'document',
        'is_verified',
        'verified_by',
        'created_at',
        'updated_at',
    ]


admin.site.register(ProofOfPayment, ProofOfPaymentAdmin)
admin.site.register(Membership, MembershipAdmin)