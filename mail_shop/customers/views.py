from django.shortcuts import render, redirect
from django.http import Http404

from customers.models import Customer
from customers.forms import CustomerForm
from packages.models import Package
from mailboxes.models import Mailbox
from transactions.models import Transaction


def index(request):
    customers = Customer.objects.all().order_by('l_name')
    context = {
        'customers': customers
    }
    return render(request, 'customers/customers_index.html', context)

def customer_view(request, customer_id):
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        raise Http404
    packages = Package.objects.filter(customer=customer)
    mailboxes = Mailbox.objects.filter(owner__owner=customer)
    transactions = Transaction.objects.filter(customer__owner=customer)
    context = {
        'customer': customer,
        'packages': packages,
        'mailboxes': mailboxes,
        'transactions': transactions,
    }
    return render(request, 'customers/customer_view.html', context)

# TODO: Refactor this view. Move customer adding bits to outside function.
# TODO: Rename to follow other views naming patterns.
def add_customer(request):
    form = CustomerForm(request.POST)
    if all([form.is_valid(), request.POST]):
        new_user = form.save()
        new_user.save()
        return  redirect('customer_view', customer_id=new_user.pk)
    context = {
        'form': form,
    }
    return render(request, 'customers/customer_form.html', context)

