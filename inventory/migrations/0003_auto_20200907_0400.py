# Generated by Django 3.1.1 on 2020-09-07 04:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20200907_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date and time when order was placed', null=True),
        ),
    ]
