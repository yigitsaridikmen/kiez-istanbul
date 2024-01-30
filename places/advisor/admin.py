from django.contrib import admin

# Register your models here.
from .models import PlaceInfo

class PlaceAdmin(admin.ModelAdmin):
    list_display = [
    'user',    
    'name',
    'address',
    'city',
    'county',
    'district',
    'place_type',
    #'activity',
    'largegroup',
    'alone',
    'dateable',
    'price_category',
    'kitchen',
    'smoke',
    'door_policy',
    'readable',
    'workable',
    'loudness',
    'comment' ,
    'created_at'
    ]
    search_fields = [    
    'name',
    'city',
    'county',
    'district',
    'place_type',
    'activity',
    'price_category',
    ]

admin.site.register(PlaceInfo,PlaceAdmin)





