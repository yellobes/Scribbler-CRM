from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from people.models import Employee, UserProfile, EmergencyContact


class EmployeeAdmin(admin.ModelAdmin):
    pass


class EmergencyContactAdmin(admin.ModelAdmin):
    search_fields = [
        'user__username',
        'user__first_name',
        'user__last_name'
    ]


class EmergencyContactInline(admin.StackedInline):
    model = EmergencyContact


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserProfileAdmin(UserAdmin):
    inlines = [
        UserProfileInline,
        EmergencyContactInline,
    ]


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmergencyContact, EmergencyContactAdmin)
