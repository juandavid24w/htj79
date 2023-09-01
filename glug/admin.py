from django.contrib import admin
from glug.models import GLUG

# Register your models here.


class GLUGAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'institute',
    ]
    readonly_fields = [
        'created_at',
        'updated_at',
    ]


admin.site.register(GLUG, GLUGAdmin)