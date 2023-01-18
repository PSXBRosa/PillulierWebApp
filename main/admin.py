from django.contrib import admin
from .models import Machine, Drug, Alarm

admin.site.site_header = 'My administration'
admin.site.register(Machine)
admin.site.register(Drug)
admin.site.register(Alarm)