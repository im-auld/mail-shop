from django.contrib import admin
from models import Mailbox, MailboxOwner


class AvailableBoxFilter(admin.SimpleListFilter):
    title = "Available Boxes"
    parameter_name = "is_owned"

    def lookups(self, request, model_admin):
        return (
            ('0', "Available"),
            ('1', "Unavailable"),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(owner__isnull=True)
        if self.value() == '1':
            return queryset.filter(owner__isnull=False)


class MailboxAdmin(admin.ModelAdmin):
    def owner_link(self, obj):
        if obj.owner:
            return '<a href="/admin/customers/customer/{}/">{}</a>'.format(
                obj.owner.id,
                obj.owner
            )
        else:
            return None

    owner_link.allow_tags = True
    owner_link.short_description = 'Owner'
    search_fields = ['box_num', 'owner__l_name']
    list_display = [
        'box_num',
        'size',
    ]
    list_filter = [
        'size',
    ]


class MailboxOwnerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Mailbox, MailboxAdmin)
admin.site.register(MailboxOwner, MailboxOwnerAdmin)
