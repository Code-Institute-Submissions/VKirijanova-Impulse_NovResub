from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import PurchaseForm
from .models import Purchase, PurchaseLineItem
from packages.models import Package
from bag.contexts import bag_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'postcode': request.POST['postcode'],
            'county': request.POST['county'],
            'country': request.POST['country'],
        }
        purchase_form = PurchaseForm(form_data)
        if purchase_form.is_valid():
            purchase = purchase_form.save()
            for item_id, item_data in bag.items():
                try:
                    package = Package.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        purchase_line_item = PurchaseLineItem(
                            purchase=purchase,
                            package=package,
                            quantity=item_data,
                        )
                        purchase_line_item.save()
                except Package.DoesNotExist:
                    messages.error(request, (
                        "Package in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[purchase.purchase_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')   
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "You didn't choose any packages yet.")
            return redirect(reverse('packages'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        purchase_form = PurchaseForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing!')

    template = 'checkout/checkout.html'
    context = {
        'purchase_form': purchase_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, purchase_number):
    save_info = request.session.get('save_info')
    purchase = get_object_or_404(Purchase, purchase_number=purchase_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {purchase_number}. A confirmation \
        email will be sent to {purchase.email} with all necessary information.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'purchase': purchase,
    }

    return render(request, template, context)