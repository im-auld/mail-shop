from django import forms
from django.forms import fields

from mailboxes.models import MailboxOwner
from packages.models import Package


class PackageForm(forms.ModelForm):
    def save(self):
        instance = super(PackageForm, self).save(commit=False)
        instance.customer = MailboxOwner.objects.get(
            box__box_num=instance.box_num.box_num).owner
        return instance

    class Meta:
        model = Package
        fields = ['box_num', 'tracking_number']


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
