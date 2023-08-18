# Generated by Django 3.2.13 on 2023-08-13 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.CharField(default=0, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(default=0, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=0, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]