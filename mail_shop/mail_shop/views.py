from datetime import date
from django.shortcuts import render

from packages.models import Package
from packages.forms import ClaimForm
from customers.models import Customer
from mailboxes.models import Mailbox, MailboxOwner


def index(request):
    claim_form = ClaimForm()
    packages = Package.objects.filter(date_claimed__isnull=True).order_by('box_num')
    alerts = MailboxOwner.objects.filter(due_date__lt=date.today())
    stats = get_stats(alerts)
    context = {
        'packages': packages,
        'alerts': alerts,
        'stats': stats,
        'claim_form': claim_form
    }
    return render(request, 'mailshop_index.html', context)

def get_stats(late):
    rented = MailboxOwner.objects.all()
    number_of_boxes = len(Mailbox.objects.all())
    overdue_percentage = round(float(len(late)) / len(rented) * 100)
    monthly_income = sum(mo.monthly_rate for mo in rented)
    percent_rented = round(float(len(late)) / number_of_boxes * 100)
    stats = {
        'overdue_percentage': overdue_percentage,
        'overdue_raw': len(late),
        'monthly_income': monthly_income,
        'percent_rented': percent_rented,
    }
    return stats


