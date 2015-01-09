from django.db import models


payment_methods = [
    (1, 'CC'),
    (2, 'Cash'),
    (3, 'Check'),
    (4, 'Store Credit'),
]

payment_types = [
    (1, 'Rent'),
    (2, 'Extra Mail Fee'),
    (3, 'Extra Package Fee'),
    (4, 'Other fee'),
]


class Payment(models.Model):
    customer = models.ForeignKey('mailboxes.MailboxOwner')
    amount = models.IntegerField()
    method = models.CharField(choices=payment_methods)
    date = models.DateField(auto_now=True)
    notes = models.CharField(max_length=250)
    payment_type = models.CharField(choices=payment_types)
