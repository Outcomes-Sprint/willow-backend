# Generated by Django 3.1.7 on 2021-03-05 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0006_donation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='date',
        ),
    ]
