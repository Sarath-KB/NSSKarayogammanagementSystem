# Generated by Django 4.2.1 on 2023-06-21 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0024_rename_member_name_tbl_chittyjoin_memberdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_paymentchitty',
            name='chitty_apply',
        ),
        migrations.RemoveField(
            model_name='tbl_paymentchitty',
            name='member',
        ),
        migrations.DeleteModel(
            name='tbl_chittyjoin',
        ),
        migrations.DeleteModel(
            name='tbl_paymentchitty',
        ),
    ]
