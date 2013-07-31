from django.contrib import admin

from rfid.models import RFIDTag


class RFIDTagAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'tag',
    )

    search_fields = [
        'user__username',
        'user__first_name',
        'user__last_name',
        'tag',
    ]

    class Meta:
        model = RFIDTag

admin.site.register(RFIDTag, RFIDTagAdmin)
