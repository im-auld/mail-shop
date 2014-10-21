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
    owner = models.ForeignKey('customers.Customer')
    box_num = models.IntegerField(unique=True, null=False)
    size = models.CharField(max_length=2, choices=BOX_SIZES)
    next_due_on = models.DateField()
    num_of_users = models.IntegerField()
    num_of_key_sets = models.IntegerField()
    used_for_business = models.BooleanField(default=False)
    is_current = models.BooleanField(default=True)

    @property
    def monthly_rate(self):
        return RATES[str(self.size)] + (self.num_of_users * 5)

    @property
    def six_month_rate(self):
        return self.monthly_rate * 6

    @property
    def yearly_rate(self):
        return self.monthly_rate * 12

    def __unicode__(self):
        return str(self.box_num)