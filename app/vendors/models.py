from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    mobile = PhoneNumberField(null=True, blank=True)
    address = models.TextField(max_length=510, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.name)


class Service(models.Model):
    class ServiceType(models.TextChoices):
        IN_ROOM_DINING = 'ird', _('In Room Dining')
        OUTLET = 'out', _('Outlet')
        RESTAURENT = 'rest', _('Restaurent')

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=ServiceType.choices, default=ServiceType.IN_ROOM_DINING)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s (%s)" % (self.name, self.type)

    class Meta:
        ordering = ['name']
