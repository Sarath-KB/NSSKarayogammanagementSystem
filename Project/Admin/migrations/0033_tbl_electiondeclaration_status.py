# Generated by Django 4.2.1 on 2023-07-13 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0032_tbl_adminlogin'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_electiondeclaration',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
