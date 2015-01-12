# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='method',
            field=models.CharField(max_length=20, choices=[(b'CC', b'CC'), (b'Cash', b'Cash'), (b'Check', b'Check'), (b'Store Credit', b'Store Credit')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='payment',
            name='notes',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(max_length=20, choices=[(b'Rent', b'Rent'), (b'Extra Mail Fee', b'Extra Mail Fee'), (b'Extra Package Fee', b'Extra Package Fee'), (b'Other Fee', b'Other fee')]),
            preserve_default=True,
        ),
    ]
