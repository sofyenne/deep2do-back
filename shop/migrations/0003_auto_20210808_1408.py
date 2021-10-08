# Generated by Django 3.0.5 on 2021-08-08 13:08

import datetime
from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210807_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 8, 14, 8, 50, 665885), null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.upload_path),
        ),
    ]