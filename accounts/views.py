from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserAccount
from .forms import UserAccountForm

from checkout.models import Purchase 


def account(request):
    """ Display the user's account. """
    account = get_object_or_404(UserAccount, user=request.user)

    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully')

    form = UserAccountForm(instance=account)
    purchases = account.purchases.all()

    template = 'accounts/account.html'
    context = {
        'form': form,
        'purchases': purchases,
        'on_account_page': True
    }

    return render(request, template, context)

def purchase_history(request, purchase_number):
    purchase = get_object_or_404(Purchase, purchase_number=purchase_number)

    messages.info(request, (
        f'This is a past confirmation for purchase number {purchase_number}. '
        'A confirmation email was sent on the purchase date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'purchase': purchase,
        'from_account': True,
    }

    return render(request, template, context)

