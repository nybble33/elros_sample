from django.contrib import admin

# Register your models here.

import cms.models as c_m


class CountryAdmin(admin.ModelAdmin):
    fields = ['name']


class ManufacturerAdmin(admin.ModelAdmin):
    fields = ['name', 'country']


class VehicleAdmin(admin.ModelAdmin):
    fields = ['name', 'manufacturer', 'start_year', 'end_year']


class CommentAdmin(admin.ModelAdmin):
    fields = ['author_email', 'vehicle', 'post_date', 'text']


admin.site.register(c_m.Country, CountryAdmin)
admin.site.register(c_m.Manufacturer, ManufacturerAdmin)
admin.site.register(c_m.Vehicle, VehicleAdmin)
admin.site.register(c_m.Comment, CommentAdmin)