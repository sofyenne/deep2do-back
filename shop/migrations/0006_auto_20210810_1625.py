# Generated by Django 3.0.5 on 2021-08-10 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210810_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 10, 16, 25, 48, 301899), null=True),
        ),
    ]
