# Generated by Django 4.2.1 on 2023-05-31 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0010_alter_tbl_memberadding_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_chitty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chitty_name', models.CharField(max_length=50)),
                ('chitty_details', models.CharField(max_length=50)),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_financehead')),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_scheme')),
            ],
        ),
    ]
