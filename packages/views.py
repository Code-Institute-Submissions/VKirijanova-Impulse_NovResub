from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Package

from .forms import PackageForm

# Create your views here.

def all_packages(request):
    """ A view to show all packages """

    packages = Package.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)


def package_detail(request, package_id):
    """ A view to show each package details """

    package = get_object_or_404(Package, pk=package_id)

    context = {
        'package': package,
    }

    return render(request, 'packages/package_detail.html', context)


@login_required
def add_package(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only gym administrator can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            package = form.save()
            messages.success(request, 'Successfully added new package.')
            return redirect(reverse('package_detail', args=[package.id]))
        else:
            messages.error(request, 'Failed to add package. Please ensure the form is valid.')
    else:
        form = PackageForm()

    template = 'packages/add_package.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_package(request, package_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only gym administrator can do that.')
        return redirect(reverse('home'))

    package = get_object_or_404(Package, pk=package_id)
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated package')
            return redirect(reverse('package_detail', args=[package.id]))
        else:
            messages.error(request, 'Failed to update package')
    else:
        form = PackageForm(instance=package)

    template = 'packages/edit_package.html'
    context = {
        'form': form,
        'package': package,
    }

    return render(request, template, context)


@login_required
def delete_package(request, package_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only gym administrator can do that.')
        return redirect(reverse('home'))

    package = get_object_or_404(Package, pk=package_id)
    package.delete()
    messages.success(request, 'Successfully deleted package')
    return redirect(reverse('packages'))



