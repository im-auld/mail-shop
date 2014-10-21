from django.contrib import admin
from models import Mailbox


class MailboxAdmin(admin.ModelAdmin):
    pass

admin.site.register(Mailbox, MailboxAdmin)
