# Generated by Django 4.2.1 on 2023-06-21 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0025_delete_tbl_electiondeclaration'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_electiondeclaration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=200)),
                ('nomination_date', models.DateField(max_length=50)),
                ('verifeid_date', models.DateField(max_length=50)),
                ('result_date', models.DateField(max_length=50)),
                ('posting_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
