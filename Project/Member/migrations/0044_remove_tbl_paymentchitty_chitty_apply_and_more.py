# Generated by Django 4.2.1 on 2023-07-15 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0043_tbl_repaymentloan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_paymentchitty',
            name='chitty_apply',
        ),
        migrations.RemoveField(
            model_name='tbl_paymentchitty',
            name='memberdata',
        ),
        migrations.RemoveField(
            model_name='tbl_paymentchitty',
            name='relative',
        ),
        migrations.DeleteModel(
            name='tbl_chittyjoin',
        ),
        migrations.DeleteModel(
            name='tbl_paymentchitty',
        ),
    ]