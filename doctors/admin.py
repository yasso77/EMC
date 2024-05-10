from django.contrib import admin
from . models import Doctor, Specialties

class DoctorAdmin(admin.ModelAdmin):
    list_display=['DoctorID','FullName','Mobile','SpecialtyID','active']
    list_display_links=['FullName']   
    search_fields=['FullName','Mobile']
# Register your models here.

admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Specialties)


    