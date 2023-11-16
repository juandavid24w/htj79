from django.contrib import admin
from software.models import Tag, Category, License, Software


# Register your models here.
class TagAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    exclude = [
        "id",
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    exclude = [
        "id",
    ]
    prepopulated_fields = {"slug": ("name",)}


class LicenseAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    exclude = [
        "id",
    ]


class SoftwareAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    exclude = [
        "id",
    ]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(Software, SoftwareAdmin)
