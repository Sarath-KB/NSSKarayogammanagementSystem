# Generated by Django 4.2.1 on 2023-06-06 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0003_rename_loannamedata_tbl_loanapply_loan_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_loanapply',
        ),
    ]