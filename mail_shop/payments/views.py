from django.shortcuts import render, redirect
from django.http import Http404
from mailboxes.models import MailboxOwner
from payments.forms import PaymentForm


def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        payment = form.save()
        payment.save()
        return redirect('customers_index')
    else:
        form = PaymentForm()
        context = {
            'form': form,
        }
        return render(request, 'payments/payment_form.html', context)
