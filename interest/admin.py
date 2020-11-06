from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from embed_video.admin import AdminVideoMixin
from .models import Item

class MyModelAdmin(AdminVideoMixin, ImportExportModelAdmin):
    list_display = ("name", "video",)

admin.site.register(Item, MyModelAdmin)