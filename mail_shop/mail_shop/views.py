from datetime import date
from django.shortcuts import render

from packages.forms import ClaimForm, get_choices
from mailboxes.models import Mailbox, MailboxOwner


def index(request):
    claim_form = ClaimForm()
    claim_form.fields['unclaimed_packages'].choices = get_choices()
    alerts = MailboxOwner.objects.filter(due_date__lt=date.today())
    stats = get_stats(alerts)
    context = {
        'alerts': alerts,
        'stats': stats,
        'claim_form': claim_form
    }
    return render(request, 'mailshop_index.html', context)

def get_stats(late):
    rented = MailboxOwner.objects.all()
    number_of_boxes = len(Mailbox.objects.all())
    overdue_percentage = round(float(len(late)) / len(rented) * 100) or 0
    monthly_income = sum(mo.monthly_rate for mo in rented)
    percent_rented = round(float(len(late)) / number_of_boxes * 100)
    stats = {
        'overdue_percentage': overdue_percentage,
        'overdue_raw': len(late),
        'monthly_income': monthly_income,
        'percent_rented': percent_rented,
    }
    return stats


