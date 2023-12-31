# Generated by Django 4.2.1 on 2023-07-15 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0033_tbl_electiondeclaration_status'),
        ('Member', '0045_tbl_chittyjoin'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_paymentchitty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repayment_date', models.DateField(auto_now_add=True)),
                ('chitty_apply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Member.tbl_chittyjoin')),
                ('memberdata', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.tbl_memberadding')),
                ('relative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Member.tbl_relatives')),
            ],
        ),
    ]
