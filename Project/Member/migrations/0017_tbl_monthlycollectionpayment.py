# Generated by Django 4.2.1 on 2023-06-14 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0016_delete_tbl_relatives'),
        ('Finance', '0009_tbl_monthlycollection'),
        ('Member', '0016_tbl_weeklycollectionpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_monthlycollectionpayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memeber_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_memberadding')),
                ('monthlycollection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finance.tbl_monthlycollection')),
            ],
        ),
    ]
