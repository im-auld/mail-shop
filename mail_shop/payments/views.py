from django.shortcuts import render, redirect
from django.http import Http404
from mailboxes.models import MailboxOwner
from payments.forms import PaymentForm


def payment_view(request, mailbox_id=None):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        payment = form.save()
        payment.save()
        return redirect('customers_index')
    else:
        data = _get_initial_form_data(mailbox_id)
        form = PaymentForm(initial=data)
        context = {
            'form': form,
        }
        return render(request, 'payments/payment_form.html', context)

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
