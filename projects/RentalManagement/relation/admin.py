from django.contrib import admin

# Register your models here.

from .models import OwnerRelation, RenterRelation

@admin.register(OwnerRelation)
class OwnerRelationadmin(admin.ModelAdmin):
    list_display = ['owner_name','owner_id']

@admin.register(RenterRelation)
class RenterRelationadmin(admin.ModelAdmin):
    list_display = ['renter_name','owner_relation','date_of_arrival']    
