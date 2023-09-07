# Generated by Django 4.2.1 on 2023-06-01 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0010_alter_tbl_memberadding_photo'),
        ('Finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_chittyjoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('chittydata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finance.tbl_chitty')),
                ('memberdata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_memberadding')),
            ],
        ),
    ]
