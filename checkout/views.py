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
        'stripe_public_key': 'pk_test_51JeS5bB206mJ1UG1uHkmJcZZTPE7GHGO6Mn1BGS1mqjPGsnFYCbZ05SaSOdFsUA3BTcWeEL0taiZjH29FxGs6GxW002aq2bllG',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)