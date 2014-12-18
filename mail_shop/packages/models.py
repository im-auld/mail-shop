from django.db import models


class Package(models.Model):
    customer = models.ForeignKey('customers.Customer')
    box_num = models.ForeignKey('mailboxes.Mailbox')
    date_arrived = models.DateField(auto_now_add=True)
    date_claimed = models.DateField(blank=True, null=True)
    tracking_number = models.CharField(max_length=25)

    def __unicode__(self):
        return str('{self.box_num} - {self.customer.l_name}'.format(self=self))
