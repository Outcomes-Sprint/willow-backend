# Generated by Django 3.1.7 on 2021-03-05 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0005_auto_20210305_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]