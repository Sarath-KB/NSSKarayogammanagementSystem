# Generated by Django 4.2.1 on 2023-06-14 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0017_tbl_monthlycollectionpayment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_monthlycollectionpayment',
            old_name='memeber_name',
            new_name='member_name',
        ),
    ]