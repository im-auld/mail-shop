import os
import datetime
from django.db import models
from django.core import validators
from sorl.thumbnail import ImageField


STATES = (
    ("AL", "Alabama"),
    ("AK", "Alaska"),
    ("AS", "American Samoa"),
    ("AZ", "Arizona"),
    ("AR", "Arkansas"),
    ("CA", "California"),
    ("CO", "Colorado"),
    ("CT", "Connecticut"),
    ("DE", "Delaware"),
    ("DC", "District Of Columbia"),
    ("FM", "Federated States Of Micronesia"),
    ("FL", "Florida"),
    ("GA", "Georgia"),
    ("GU", "Guam"),
    ("HI", "Hawaii"),
    ("ID", "Idaho"),
    ("IL", "Illinois"),
    ("IN", "Indiana"),
    ("IA", "Iowa"),
    ("KS", "Kansas"),
    ("KY", "Kentucky"),
    ("LA", "Louisiana"),
    ("ME", "Maine"),
    ("MH", "Marshall Islands"),
    ("MD", "Maryland"),
    ("MA", "Massachusetts"),
    ("MI", "Michigan"),
    ("MN", "Minnesota"),
    ("MS", "Mississippi"),
    ("MO", "Missouri"),
    ("MT", "Montana"),
    ("NE", "Nebraska"),
    ("NV", "Nevada"),
    ("NH", "New Hampshire"),
    ("NJ", "New Jersey"),
    ("NM", "New Mexico"),
    ("NY", "New York"),
    ("NC", "North Carolina"),
    ("ND", "North Dakota"),
    ("MP", "Northern Mariana Islands"),
    ("OH", "Ohio"),
    ("OK", "Oklahoma"),
    ("OR", "Oregon"),
    ("PW", "Palau"),
    ("PA", "Pennsylvania"),
    ("PR", "Puerto Rico"),
    ("RI", "Rhode Island"),
    ("SC", "South Carolina"),
    ("SD", "South Dakota"),
    ("TN", "Tennessee"),
    ("TX", "Texas"),
    ("UT", "Utah"),
    ("VT", "Vermont"),
    ("VI", "Virgin Islands"),
    ("VA", "Virginia"),
    ("WA", "Washington"),
    ("WV", "West Virginia"),
    ("WI", "Wisconsin"),
    ("WY", "Wyoming")
)


def get_owner_path(instance, filename):
    parts = [instance.owner.l_name]
    parts.append(os.path.basename(filename))
    path = u"/".join(parts)
    return path


class Photo(models.Model):
    photo_file = ImageField(
        upload_to=get_owner_path,
    )
    owner = models.ForeignKey('Customer')


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
    state = models.CharField(max_length=2, choices=STATES)
    phone_num = models.CharField(
        'phone number',
        max_length=15,
    )
    photo_file = models.OneToOneField(
        Photo,
        related_name='customer',
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return '{self.f_name} {self.l_name}'.format(self=self)