from django.contrib import admin
from models import Mailbox


class MailboxAdmin(admin.ModelAdmin):
    search_fields = ['box_num', 'owner__l_name', 'owner__email']

admin.site.register(Mailbox, MailboxAdmin)
