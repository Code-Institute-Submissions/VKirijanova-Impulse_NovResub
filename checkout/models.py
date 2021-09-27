import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from packages.models import Package

class Purchase(models.Model):
    purchase_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = models.CharField(max_length=40, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def generate_purchase_number(self):
        """ Generate unique number (using UUID) """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Update grand total each time a line item is added """
        self.purchase_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']

        self.grand_total = self.purchase_total
        self.save()

    def save(self, *args, **kwargs):
        """ Override the original save method if it hasn't been set already """
        if not self.purchase_number:
            self.purchase_number = self._generate_purchase_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.purchase_number

class PurchaseLineItem(models.Model):
    purchase = models.ForeignKey(Purchase, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Package, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """ Override the original save method to set the lineitem total and update the order total """
        self.lineitem_total = self.package.price * self.quantity
        super().save(*args, **kwargs) 

    def __str__(self):
        return f'SKU {self.package.sku} on order {self.purchase.purchase_number}'