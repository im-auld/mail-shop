from django.contrib import admin
from payments.models import Payment


class PaymentAdmin(admin.ModelAdmin):
    search_fields = ['customer', 'method', 'date', 'payment_type']
    list_display = ['customer', 'amount', 'method', 'date', 'payment_type']
    list_filter = ['customer', 'amount', 'method', 'date', 'payment_type']

admin.site.register(Payment, PaymentAdmin)
