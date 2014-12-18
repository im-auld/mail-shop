from django.shortcuts import render
from models import Customer
from packages.models import Package
from mailboxes.models import Mailbox


def index(request):
    customers = Customer.objects.all().order_by('l_name')
    context = {
        'customers': customers
    }
    return render(request, 'customers/index.html', context)

def customer_view(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    packages = Package.objects.filter(customer=customer)
    mailboxes = Mailbox.objects.filter(owner__owner=customer)
    context = {
        'customer': customer,
        'packages': packages,
        'mailboxes': mailboxes
    }
    return render(request, 'customers/customer_view.html', context)
