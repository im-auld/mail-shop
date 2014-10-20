from django.db import models


class Package(models.Model):
    customer = models.ForeignKey('customer.Customer')
    box_num = models.ForeignKey('mailboxes.Mailbox')
    date_arrived = models.DateField(auto_now_add=True)
    date_claimed = models.DateField(blank=True)
    tracking_number = models.CharField()

    def __init__(self, customer, box_num, tracking_number):
        self.customer = customer
        self.box_num = box_num
        self.tracking_number = tracking_number
