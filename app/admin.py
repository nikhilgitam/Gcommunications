from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from app.models import *

admin.site.register(PushNotificationStatus)
admin.site.register(PushToken)
admin.site.register(GroupList)
admin.site.register(WebApplication)
admin.site.register(WebNotificationStatus)
admin.site.register(MobileApplication)
admin.site.register(UploadImage)

@admin.register(Dean)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ('college', 'stream')
    search_fields = ('college', 'stream')


@admin.register(Category)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(PushNotification)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ('campus', 'institute','department','dt_time')
    search_fields = ('campus', 'institute','title')