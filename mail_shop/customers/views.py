from django.shortcuts import render
from models import Customer


def index(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'customers/index.html', context)

def customer_view(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    context = {
        'customer': customer,
    }
    return render(request, 'customers/customer_view.html', context)
