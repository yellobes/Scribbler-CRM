from django.contrib import admin

from rfid.models import RFIDTag


class RFIDTagAdmin(admin.ModelAdmin):
    class Meta:
        model = RFIDTag

admin.site.register(RFIDTag, RFIDTagAdmin)
