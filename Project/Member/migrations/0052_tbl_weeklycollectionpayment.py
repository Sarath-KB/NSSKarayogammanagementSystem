# Generated by Django 4.2.1 on 2023-07-15 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0033_tbl_electiondeclaration_status'),
        ('Finance', '0009_tbl_monthlycollection'),
        ('Member', '0051_delete_tbl_weeklycollectionpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_weeklycollectionpayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repayment_date', models.DateField(auto_now_add=True)),
                ('member_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.tbl_memberadding')),
                ('relative_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Member.tbl_relatives')),
                ('weeklycollection_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finance.tbl_weeklycollection')),
            ],
        ),
    ]
