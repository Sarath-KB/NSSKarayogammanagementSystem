# Generated by Django 4.2.1 on 2023-06-21 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0009_tbl_monthlycollection'),
        ('Admin', '0023_alter_tbl_memberadding_password'),
        ('Member', '0025_remove_tbl_paymentchitty_chitty_apply_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_chittyjoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('document', models.FileField(upload_to='Doc/')),
                ('chittydata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finance.tbl_chitty')),
                ('memberdata', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.tbl_memberadding')),
                ('proof_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_proof')),
                ('relative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Member.tbl_relatives')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_paymentchitty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chitty_apply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Member.tbl_chittyjoin')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_memberadding')),
            ],
        ),
    ]