# Generated by Django 4.2.1 on 2023-07-09 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0031_tbl_events'),
        ('Member', '0031_complaint'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='complaint',
            new_name='tbl_complaint',
        ),
    ]
