from django import forms
from payments.models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        widgets = {
            'notes': forms.Textarea()
        }
        fields = ['customer', 'amount', 'method', 'payment_type', 'notes']
