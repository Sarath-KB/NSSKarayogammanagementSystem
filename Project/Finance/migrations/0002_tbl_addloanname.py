# Generated by Django 4.2.1 on 2023-06-02 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_tbl_loan'),
        ('Finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_addloanname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_name', models.CharField(max_length=50)),
                ('loan_details', models.CharField(max_length=50)),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_financehead')),
                ('loan_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_loan')),
            ],
        ),
    ]
