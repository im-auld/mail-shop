from django.db import models


payment_methods = [
    ('CC', 'CC'),
    ('Cash', 'Cash'),
    ('Check', 'Check'),
    ('Store Credit', 'Store Credit'),
]

transaction_types = [
    ('Payment', 'Payment'),
    ('Fee', 'Fee')
]

transaction_reasons = [
    ('Rent', 'Rent'),
    ('Extra Mail', 'Extra Mail'),
    ('Extra Package', 'Extra Package'),
    ('Other', 'Other'),
]


class Transaction(models.Model):
    customer = models.ForeignKey('mailboxes.MailboxOwner')
    amount = models.IntegerField()
    date = models.DateField(auto_now=True)
    transaction_type = models.CharField(
        max_length=20,
        choices=transaction_types
    )
    transaction_reason = models.CharField(
        max_length=20,
        choices=transaction_reasons
    )
    payment_method = models.CharField(
        max_length=20,
        choices=payment_methods,
        blank=True,
        null=True,
    )
    notes = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )

    def validate_transaction(self):
        if self.transaction_type == 'Payment' and not self.payment_method:
            return False
        return True
