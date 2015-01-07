from django import forms
from django.forms import fields

from packages.models import Package


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['customer', 'box_num', 'tracking_number']


class ClaimForm(forms.Form):
    unclaimed_packages = fields.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'package-list-item'}
        ),
        choices=[
            (p.pk, '{p} - {p.tracking_number}'.format(p=p))
                for p in Package.objects.filter(date_claimed__isnull=True)
        ],
    )
    pin = fields.IntegerField(widget=forms.PasswordInput)
