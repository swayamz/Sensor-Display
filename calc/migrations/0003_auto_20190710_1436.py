# Generated by Django 2.2.2 on 2019-07-10 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_auto_20190706_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmdata',
            name='group',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='farmdata',
            name='variable',
            field=models.IntegerField(),
        ),
    ]
