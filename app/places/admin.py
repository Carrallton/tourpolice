from django.contrib import admin
from .models  import Place

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'latitude', 'longitude')
    search_fields = ('name', 'address')
    list_filter = ('name',)
    ordering = ('name',)

admin.site.register(Place, PlacesAdmin)