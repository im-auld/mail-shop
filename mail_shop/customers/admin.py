from django.contrib import admin
from models import Customer


class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['l_name', 'phone_num', 'email']
    #readonly_fields = ('upload_date', 'modified_date', 'published_date',)
    list_display = ('l_name', 'f_name', 'email', 'phone_num')

admin.site.register(Customer, CustomerAdmin)