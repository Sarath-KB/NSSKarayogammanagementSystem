# Generated by Django 4.2.1 on 2023-06-07 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0013_rename_loan_name_tbl_proof_proof_name'),
        ('Member', '0009_delete_tbl_repaymentloan'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_repaymentloan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loanapply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Member.tbl_loanapply')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_memberadding')),
            ],
        ),
    ]
