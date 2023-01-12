from django.contrib import admin
from .models import Drug, Alarm, DrugsOnAlarm

admin.site.site_header = 'My administration'
admin.site.register(Drug)
admin.site.register(Alarm)
admin.site.register(DrugsOnAlarm)