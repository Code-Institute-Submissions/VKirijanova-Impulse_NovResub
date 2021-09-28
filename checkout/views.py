from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import PurchaseForm
from .models import Purchase, PurchaseLineItem
from packages.models import Package
from accounts.forms import UserAccountForm
from accounts.models import UserAccount
from bag.contexts import bag_contents

import stripe
import json

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

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
            purchase = purchase_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            purchase.stripe_pid = pid
            purchase.original_bag = json.dumps(bag)
            purchase.save()
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

        if request.user.is_authenticated:
            try:
                account = UserAccount.objects.get(user=request.user)
                purchase_form = PurchaseForm(initial={
                    'full_name': account.user.get_full_name(),
                    'email': account.user.email,
                    'phone_number': account.default_phone_number,
                    'country': account.default_country,
                    'postcode': account.default_postcode,
                    'town_or_city': account.default_town_or_city,
                    'street_address1': account.default_street_address1,
                    'street_address2': account.default_street_address2,
                    'county': account.default_county,
                })
            except UserAccount.DoesNotExist:
                purchase_form = PurchaseForm()
        else:
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
    
    if request.user.is_authenticated:
        account = UserAccount.objects.get(user=request.user)
        purchase.user_account = account
        purchase.save()

        if save_info:
            account_data = {
                'default_phone_number': purchase.phone_number,
                'default_country': purchase.country,
                'default_postcode': purchase.postcode,
                'default_town_or_city': purchase.town_or_city,
                'default_street_address1': purchase.street_address1,
                'default_street_address2': purchase.street_address2,
                'default_county': purchase.county,
            }
            user_account_form = UserAccountForm(account_data, instance=account)
            if user_account_form.is_valid():
                user_account_form.save()
    
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