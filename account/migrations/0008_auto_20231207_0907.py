# Generated by Django 3.2.13 on 2023-12-07 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='account_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='account_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
