# Generated by Django 4.2.1 on 2023-07-15 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0048_tbl_repaymentloan'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_weeklycollectionpayment',
        ),
    ]
