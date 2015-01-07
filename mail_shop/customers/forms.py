from django.forms import ModelForm
from customers.models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'f_name',
            'l_name',
            'line_1',
            'line_2',
            'city',
            'state',
            'zip_code',
            'phone_num',
            'email',
            'photo_file'
        ]
