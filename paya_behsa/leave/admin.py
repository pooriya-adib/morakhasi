from django.contrib.auth.models import Group, User
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Leave, LeaveRestriction, Driver
from .resources import DriverResource


class LeaveAdmin(admin.ModelAdmin):
    list_display = ('nation_code', 'mobile_number', 'start_date', 'end_date', 'city_travel_destination',
                    'state_travel_destination', 'city_origin_trip', 'state_origin_trip', 'status')
    search_fields = ['nation_code', 'mobile_number', 'status', 'start_date', 'end_date', 'city_travel_destination',
                     'state_travel_destination', 'city_origin_trip', 'state_origin_trip']
    list_display_links = ['nation_code', 'mobile_number', 'start_date', 'end_date', 'city_travel_destination',
                          'state_travel_destination', 'city_origin_trip', 'state_origin_trip']
    list_editable = ('status',)


class LeaveRestrictionAdmin(admin.ModelAdmin):
    list_display = ('day_per_year',)
    search_fields = ('day_per_year',)

    def save_model(self, request, obj, form, change):
        # Check if there is already an existing record
        if LeaveRestriction.objects.exists():
            day = LeaveRestriction.objects.first().day_per_year
            day = obj.day_per_year - day
            drivers = Driver.objects.all()
            for driver in drivers:
                driver.leave_restriction += day
                if driver.leave_restriction < 0:
                    driver.leave_restriction = 0
                driver.save()
            # If it exists, delete it
            LeaveRestriction.objects.all().delete()
            # Now save the new object
        obj.save()


@admin.register(Driver)
class DriverAdmin(ImportExportModelAdmin):
    resource_class = DriverResource
    list_display = ('name', 'family', 'father_name', 'city_code', 'three_len_code', 'alphabet', 'two_len_code',
                    'car', 'mobile_number', 'nation_code')
    list_display_links = ('name', 'family', 'father_name', 'city_code', 'three_len_code', 'alphabet', 'two_len_code',
                          'car', 'mobile_number', 'nation_code')
    search_fields = ('name', 'family', 'father_name', 'city_code', 'three_len_code', 'alphabet', 'two_len_code',
                     'car', 'mobile_number', 'nation_code')


admin.site.register(Leave, LeaveAdmin)
admin.site.register(LeaveRestriction, LeaveRestrictionAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
