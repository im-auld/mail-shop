from django.contrib import admin
from transactions.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    search_fields = [
        'customer',
        'payment_method',
        'date',
        'transaction_type',
        'transaction_reason'
    ]
    list_display = [
        'customer',
        'date',
        'transaction_type',
        'transaction_reason',
    ]
    list_filter = [
        'customer',
        'payment_method',
        'date',
        'transaction_type',
        'transaction_reason'
    ]

admin.site.register(Transaction, TransactionAdmin)
