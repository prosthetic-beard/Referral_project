# Generated by Django 3.2.13 on 2023-08-13 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_transactions'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='balance',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transactions',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('PC', 'Processing'), ('A', 'Approved'), ('D', 'Denied')], default='P', max_length=2),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.DecimalField(decimal_places=4, max_digits=15),
        ),
    ]
