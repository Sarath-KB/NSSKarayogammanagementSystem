# Generated by Django 4.2.1 on 2023-06-06 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0002_tbl_addloanname'),
        ('Admin', '0013_rename_loan_name_tbl_proof_proof_name'),
        ('Member', '0006_delete_tbl_chittyjoin'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_chittyjoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('document', models.FileField(upload_to='Doc/')),
                ('chittydata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finance.tbl_chitty')),
                ('memberdata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_memberadding')),
                ('proof_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_proof')),
            ],
        ),
    ]
