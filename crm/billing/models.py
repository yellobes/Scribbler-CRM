from decimal import Decimal
from django.db import models
from django.contrib import humanize

from django_measurement.fields import MeasurementField
from django_measurement.measure import Weight


try:
    from south.modelsinspector import add_introspection_rules
except ImportError:
    SOUTH = False
else:
    SOUTH = True


class CurrencyField(models.DecimalField):
    __metaclass__ = models.SubfieldBase

    def __init__(self, verbose_name=None, name=None, **kwargs):
        decimal_places = kwargs.pop('decimal_places', 2)
        max_digits = kwargs.pop('max_digits', 10)

        super(CurrencyField, self). __init__(
            verbose_name=verbose_name, name=name, max_digits=max_digits,
            decimal_places=decimal_places, **kwargs)

    def to_python(self, value):
        try:
            return super(CurrencyField, self).to_python(value).quantize(Decimal("0.01"))
        except AttributeError:
            return None



class Product(models.Model):
    name = models.CharField(max_length=255)
    price = CurrencyField()

    def __unicode__(self):
        return self.name


class Consumable(Product):
    unit = MeasurementField()


class Donation(models.Model):
    user = models.ForeignKey('auth.User')
    amount = CurrencyField()
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s donated $%s" % (self.user, self.amount)


class Purchace(models.Model):
    user = models.ForeignKey('auth.User')
    product = models.ForeignKey(Product)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s bought %s" % (self.user, self.product)

