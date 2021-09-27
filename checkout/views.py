from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import PurchaseForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "You didn't choose any packages yet.")
        return redirect(reverse('packages'))

    purchase_form = PurchaseForm()
    template = 'checkout/checkout.html'
    context = {
        'purchase_form': purchase_form,
    }

    return render(request, template, context)