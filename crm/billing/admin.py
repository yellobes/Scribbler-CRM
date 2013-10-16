from django.contrib import admin

from django_measurement.admin import MeasurementAdmin

from billing.models import Product, Donation, Purchace, Consumable


class ConsumableAdmin(MeasurementAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    search_fields = ('name', 'price')


class DonationAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'date',)


class PurchaceAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'date',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Purchace)
admin.site.register(Consumable, ConsumableAdmin)
