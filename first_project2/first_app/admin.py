from django.contrib import admin
from .models import Destination
# Register your models here.

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    list_filter = ('name',)
    search_fields = ('name','price')
    
