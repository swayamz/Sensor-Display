# Generated by Django 2.2.2 on 2019-07-12 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_farmdatajson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmdata',
            name='group',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='farmdata',
            name='time',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='farmdata',
            name='variable',
            field=models.CharField(max_length=15),
        ),
    ]
