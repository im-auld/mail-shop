from django.shortcuts import render, redirect
from django.http import Http404

from packages.models import Package
from packages.forms import PackageForm


def index(request):
    packages = Package.objects.all()
    context = {
        'packages': packages,
    }
    return render(request, 'packages/index.html', context)

def package_view(request, package_id):
    try:
        package = Package.objects.get(pk=package_id)
    except Package.DoesNotExist:
        raise Http404
    context = {
        'package': package,
        'customer': package.customer,
        'page_title': 'Package for {customer.l_name}'.format(
            customer=package.customer
        )
    }
    return render(request, 'packages/package_view.html', context)

def package_form_view(request):
    form = PackageForm()
    context = {
        'form': form,
    }
    return render(request, 'packages/package_form.html', context)
