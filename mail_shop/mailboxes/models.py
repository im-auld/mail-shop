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
    owner = models.ForeignKey('mailboxes.MailboxOwner', null=True, blank=True)
    box_num = models.IntegerField('Box Number', unique=True, null=False)
    size = models.CharField(max_length=2, choices=BOX_SIZES)

    class Meta:
        verbose_name_plural = 'Mailboxes'

    def __unicode__(self):
        return str(self.box_num)

    def __str__(self):
        return str(self.box_num)


class MailboxOwner(models.Model):
    box = models.ForeignKey('mailboxes.Mailbox')
    owner = models.ForeignKey('customers.Customer')
    start_date = models.DateField('Owned Since: ')
    due_date = models.DateField('Next Bill Due: ')
    num_additional_users = models.IntegerField('Additional users: ', default=0)
    num_of_key_sets = models.IntegerField('Sets of keys: ', default=1)
    used_for_business = models.BooleanField('Used for business', default=False)
    is_current = models.BooleanField('Current', default=True)

    def __unicode__(self):
        return '{o.owner} - Box: {o.box}'.format(o=self)

    @property
    def monthly_rate(self):
        return (
            RATES[str(self.mailbox.size)] +
            (self.num_additional_users * 5) +
            (int(self.used_for_business * 5))
        )

    @property
    def six_month_rate(self):
        return self.monthly_rate * 6

    @property
    def yearly_rate(self):
        return self.monthly_rate * 12

    @property
    def is_owned(self):
        return True
