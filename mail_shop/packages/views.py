from django.shortcuts import render
from django.http import Http404

from packages.models import Package


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
    customer = package.customer
    context = {
        'package': package,
        'customer': customer,
        'page_title': 'Package for {customer.l_name}'.format(customer=customer)
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
