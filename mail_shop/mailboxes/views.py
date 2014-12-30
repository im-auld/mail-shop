from datetime import date
from django.shortcuts import render, redirect
from django.http import Http404

from mailboxes.models import Mailbox


def index(request):
    mailboxes = Mailbox.objects.all()
    context = {
        'mailboxes': mailboxes,
    }
    return render(request, 'mailboxes/index.html', context)

def mailbox_view(request, mailbox_id):
    try:
        mailbox = Mailbox.objects.get(pk=mailbox_id)
    except:
        raise Http404
    owner = mailbox.owner
    if owner:
        owner.is_current = owner.due_date > date.today()
    else:
        owner = None
    context = {
        'mailbox': mailbox,
        'owner': owner,
        'page_title': 'Mailbox {} Details'.format(mailbox.box_num)
    }
    return render(request, 'mailboxes/mailbox_view.html', context)
