# Generated by Django 4.2.1 on 2023-06-20 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0020_tbl_electionposition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_memberadding',
            name='password',
            field=models.CharField(default=1234, max_length=50),
        ),
    ]
