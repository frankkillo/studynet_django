from django.contrib import admin

from .models import Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['course', 'lesson', 'status', 'created_by']


admin.site.register(Activity, ActivityAdmin)