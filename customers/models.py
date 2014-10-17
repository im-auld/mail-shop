from django.db import models
from django.core import validators
from sorl.thumbnail import ImageField

STATES = (
    ('AZ', 'Arizona'),
    ('AK', 'Arkansas'),
    ('NY', 'New York'),
    ('WA', 'Washington'),
)


ID_TYPES = (
    ('DL', 'Drivers License'),
    ('ND', 'State Non-Driver ID'),
    ('CC', 'Credit/Debit Card'),
    ('ST', 'Student ID'),
    ('OT', 'Other'),
)


class Customer(models.Model):
    f_name = models.CharField(
        'first name',
        max_length=25,
        help_text='Required. 25 characters or fewer',
        validators=[
            validators.MaxLengthValidator(25)
        ]
    )
    l_name = models.CharField(
        'last name',
        max_length=25,
        help_text='Required. 25 characters or fewer',
        validators=[
            validators.MaxLengthValidator(25)
        ]
    )
    line_1 = models.CharField('Address Line 1', max_length=50)
    line_2 = models.CharField('Address Line 2', max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(choices=STATES)
    phone_num = models.CharField(
        'phone number',
        max_length=15,
    )
    first_id = models.CharField(choices=ID_TYPES)
    second_id = models.CharField(choices=ID_TYPES)
    first_id_image = ImageField(upload_to=)