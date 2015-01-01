from django.forms import ModelForm

from packages.models import Package


class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = ['customer', 'box_num', 'tracking_number']
