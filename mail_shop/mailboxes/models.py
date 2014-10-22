from datetime import datetime
from django.db import models


BOX_SIZES = (
    ('SM', 'SM'),
    ('MD', 'MD'),
    ('LG', 'LG'),
)

RATES = {
    'SM': 15,
    'MD': 20,
    'LG': 25
}


class Mailbox(models.Model):
    owner = models.ForeignKey('customers.Customer', blank=True, null=True)
    box_num = models.IntegerField('Box Number', unique=True, null=False)
    size = models.CharField(max_length=2, choices=BOX_SIZES)
    owned_since = models.DateField('Owned Since: ', blank=True, null=True)
    next_due_on = models.DateField('Next Bill Due: ', blank=True, null=True)
    num_of_users = models.IntegerField('Additional users: ', default=0)
    num_of_key_sets = models.IntegerField('Sets of keys: ', default=1)
    used_for_business = models.BooleanField('Used for business', default=False)
    is_current = models.BooleanField('Current', default=True)

    class Meta:
        verbose_name_plural = 'Mailboxes'

    @property
    def monthly_rate(self):
        return RATES[str(self.size)] + (self.num_of_users * 5) + (int(self.used_for_business * 5))

    @property
    def six_month_rate(self):
        return self.monthly_rate * 6

    @property
    def yearly_rate(self):
        return self.monthly_rate * 12

    @property
    def is_owned(self):
        return bool(self.owner)

    def __unicode__(self):
        return str(self.box_num)

    def __str__(self):
        return str(self.box_num)