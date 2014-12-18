from django.shortcuts import render
from models import Customer


def index(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'customers/index.html', context)
