# Generated by Django 4.2.1 on 2023-07-28 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0033_tbl_electiondeclaration_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_memberadding',
            name='inactive',
            field=models.IntegerField(default=0),
        ),
    ]
