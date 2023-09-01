from django.contrib import admin
from institutions.models import Institutions

# Register your models here.


class InstitutionsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    readonly_fields = [
        'created_at',
        'updated_at',
    ]


admin.site.register(Institutions, InstitutionsAdmin)
