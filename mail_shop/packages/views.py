from datetime import date
from django.shortcuts import render, redirect
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

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
    if request.method == 'POST':
        form = PackageForm(request.POST)
        new_package = form.save()
        new_package.save()
        return redirect('packages_index')
    else:
        form = PackageForm()
        context ={
            'form': form,
            'page_title': 'Add Package'
        }
        return render(request, 'packages/package_form.html', context)


def claim_packages_view(request):
    if request.method == 'POST':
        package_ids = request.POST.getlist('claimed_packages[]', [])
        print package_ids
        for package_id in package_ids:
            package = Package.objects.get(pk=package_id)
            package.date_claimed = date.today()
            package.save()
    return redirect('index')
