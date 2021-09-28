from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserAccount
from .forms import UserAccountForm


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
