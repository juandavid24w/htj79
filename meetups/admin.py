from django.contrib import admin
from meetups.models import Meetups

# Register your models here.


class MeetupAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "glug",
        "date",
        "author",
    )
    prepopulated_fields = {"slug": ("title")}


admin.site.register(Meetups, MeetupAdmin)
