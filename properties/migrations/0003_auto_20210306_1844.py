# Generated by Django 3.1.7 on 2021-03-06 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20210305_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='documentation',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='property',
            name='foreclosure_status',
            field=models.CharField(choices=[('Pre-Foreclosure', 'Pre-Foreclosure'), ('Payment Default', 'Payment Default'), ('Notice of Default', 'Notice of Default'), ("Notice of Trustee's Sale", "Notice of Trustee's Sale"), ("Trustee's Sale", "Trustee's Sale"), ('Real Estate Owned(REO)', 'Real Estate Owned(REO)'), ('Eviction', 'Eviction')], default='Pre-Foreclosure', max_length=30),
        ),
        migrations.AddField(
            model_name='property',
            name='missed_payments',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='monthly_payment',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='owner',
            field=models.CharField(default='default=string', max_length=255),
            preserve_default=False,
        ),
    ]
