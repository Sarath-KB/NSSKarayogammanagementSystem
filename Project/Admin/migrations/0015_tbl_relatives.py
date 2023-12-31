# Generated by Django 4.2.1 on 2023-06-08 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0014_tbl_relationtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_relatives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relative_name', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('photo', models.FileField(upload_to='doc/')),
                ('refer_id', models.IntegerField(max_length=50)),
                ('member_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_memberadding')),
                ('relation_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_relationtype')),
            ],
        ),
    ]
