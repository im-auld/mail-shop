from django.db import models


payment_methods = [
    ('CC', 'CC'),
    ('Cash', 'Cash'),
    ('Check', 'Check'),
    ('Store Credit', 'Store Credit'),
]

payment_types = [
    ('Rent', 'Rent'),
    ('Extra Mail Fee', 'Extra Mail Fee'),
    ('Extra Package Fee', 'Extra Package Fee'),
    ('Other Fee', 'Other fee'),
]


class Payment(models.Model):
    customer = models.ForeignKey('mailboxes.MailboxOwner')
    amount = models.IntegerField()
    date = models.DateField(auto_now=True)
    payment_type = models.CharField(max_length=20, choices=payment_types)
    method = models.CharField(max_length=20, choices=payment_methods)
    notes = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
