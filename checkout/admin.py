from django.contrib import admin
from .models import Purchase, PurchaseLineItem

class PurchaseLineItemAdminInline(admin.TabularInline):
    model = PurchaseLineItem
    readonly_fields = ('lineitem_total',)

class PurchaseAdmin(admin.ModelAdmin):
    inlines = (PurchaseLineItemAdminInline,)

    readonly_fields = ('purchase_number', 'date',
                       'grand_total',)

    fields = ('purchase_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'grand_total',)

    list_display = ('purchase_number', 'date', 'full_name',
                    'grand_total',)

    ordering = ('-date',)

admin.site.register(Purchase, PurchaseAdmin)