# Generated by Django 2.1.4 on 2018-12-29 01:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankaccount',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='account_opened',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 28, 19, 40, 54, 177327)),
        ),
    ]
