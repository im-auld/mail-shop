from django.shortcuts import render
from packages.models import Package



def index(request):
    packages = Package.objects.all()
    context = {
        'packages': packages,
    }
    return render(request, 'packages/index.html', context)
