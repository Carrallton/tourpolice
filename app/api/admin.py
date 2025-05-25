from django.contrib import admin
from .models import News, EmergencyRequest

class EmergencyRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'lat', 'lon', 'emergency_type', 'timestamp')
    list_filter = ('emergency_type', 'timestamp')
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)

admin.site.register(EmergencyRequest, EmergencyRequestAdmin)