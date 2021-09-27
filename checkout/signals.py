from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import PurchaseLineItem

@receiver(post_save, sender=PurchaseLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update purchase total on lineitem update/create
    """
    instance.purchase.update_total()

@receiver(post_delete, sender=PurchaseLineItem)
def update_on_save(sender, instance, **kwargs):
    """
    Update purchase total on lineitem delete
    """
    instance.purchase.update_total()