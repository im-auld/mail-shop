from django.shortcuts import render, redirect
from django.http import Http404

from mailboxes.models import MailboxOwner
from transactions.forms import TransactionForm


def transaction_view(request, mailbox_id=None):
    if request.method == 'POST':
        transaction = TransactionForm(request.POST).save()
        transaction.save()
        return redirect('customers_index')
    else:
        data = _get_initial_form_data(mailbox_id)
        form = TransactionForm(initial=data)
        context = {
            'form': form,
        }
        return render(request, 'transactions/transaction_form.html', context)

def _get_initial_form_data(mailbox_id):
    try:
        customer = MailboxOwner.objects.get(box__pk=mailbox_id)
        data = {
            'customer': customer.pk,
            'amount': customer.monthly_rate,
            'payment_type': 'Rent'
        }
        return data
    except MailboxOwner.DoesNotExist:
        return {}

def _apply_payment(payment):
    owner = MailboxOwner.objects.get(owner=payment.customer)
