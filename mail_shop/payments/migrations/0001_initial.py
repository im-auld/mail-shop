# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailboxes', '0003_remove_mailboxowner_pin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('method', models.CharField(max_length=20, choices=[(1, b'CC'), (2, b'Cash'), (3, b'Check'), (4, b'Store Credit')])),
                ('date', models.DateField(auto_now=True)),
                ('notes', models.CharField(max_length=250)),
                ('payment_type', models.CharField(max_length=20, choices=[(1, b'Rent'), (2, b'Extra Mail Fee'), (3, b'Extra Package Fee'), (4, b'Other fee')])),
                ('customer', models.ForeignKey(to='mailboxes.MailboxOwner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
