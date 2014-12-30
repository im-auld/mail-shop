from django.shortcuts import render, redirect

from mailboxes.models import Mailbox


def index(request):
    mailboxes = Mailbox.objects.all()
    context = {
        'mailboxes': mailboxes,
    }
    return render(request, 'mailboxes/index.html', context)

def mailbox_view(request, mailbox_id):
    mailbox = Mailbox.objects.get(pk=mailbox_id)
    context = {
        'mailbox': mailbox
    }
    return render(request, 'mailboxes/mailbox_view.html', context)
