from django.contrib import admin

from people.models import Employee, UserProfile, EmergencyContact


class EmployeeAdmin(admin.ModelAdmin):
    pass


class EmergencyContactAdmin(admin.ModelAdmin):
    pass


class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(EmergencyContact, EmergencyContactAdmin)
