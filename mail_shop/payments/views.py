from django.shortcuts import render, redirect
from django.http import Http404
from mailboxes.models import MailboxOwner
from payments.forms import PaymentForm


def payment_view(request, mailbox_id):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        payment = form.save()
        payment.save()
        return redirect('customers_index')
    else:
        print(mailbox_id)
        # import pdb; pdb.set_trace()
        customer = MailboxOwner.objects.get(box__pk=1)
        form = PaymentForm(initial={
            'customer': customer.pk,
            'amount': customer.monthly_rate,
            'payment_type': 'Rent'
        })
        context = {
            'form': form,
        }
        return render(request, 'payments/payment_form.html', context)
