from django.contrib import admin
from .models import Court, CourtPhoto, City, District, Address

class CourtPhotoInline(admin.TabularInline):
	model = CourtPhoto
	extra = 3

class CourtAdmin(admin.ModelAdmin):
	inlines = [ CourtPhotoInline, ]

admin.site.register(Court, CourtAdmin)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Address)