# Generated by Django 3.0.5 on 2021-07-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='numberofvisitors',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
