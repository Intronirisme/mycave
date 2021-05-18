from django.contrib import admin
from showroom.models import Wine

# Register your models here.

@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'country', 'id')
    search_fields = ('name', 'year', 'country')