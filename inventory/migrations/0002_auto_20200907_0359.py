# Generated by Django 3.1.1 on 2020-09-07 03:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 7, 3, 59, 57, 270021, tzinfo=utc), help_text='Date and time when order was placed', null=True),
        ),
    ]
