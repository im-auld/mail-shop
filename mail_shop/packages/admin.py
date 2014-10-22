from django.contrib import admin
from models import Package


class ClaimedPackagesFilter(admin.SimpleListFilter):
    title = "Claimed"
    parameter_name = "is_claimed"

    def lookups(self, request, model_admin):
        return (
            ('0', "Unclaimed"),
            ('1', "Claimed"),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(date_claimed__isnull=True)
        if self.value() == '1':
            return queryset.filter(date_claimed__isnull=False)


class PackageAdmin(admin.ModelAdmin):
    list_display = [
        'box_num',
        'customer',
        'date_arrived',
        'date_claimed',
        'tracking_number'
    ]
    list_filter = ['box_num', 'date_arrived', ClaimedPackagesFilter]
    search_fields = ['customer', 'tracking_number']


admin.site.register(Package, PackageAdmin)
