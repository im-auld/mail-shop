from django import forms
from transactions.models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        widgets = {
            'notes': forms.Textarea()
        }
        fields = [
            'customer',
            'amount',
            'payment_method',
            'transaction_type',
            'transaction_reason',
            'notes',
        ]
