# Generated by Django 4.0 on 2022-01-06 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_date_created_customer_datecreated_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
    ]
