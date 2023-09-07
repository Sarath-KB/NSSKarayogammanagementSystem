# Generated by Django 4.2.1 on 2023-07-09 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0031_tbl_events'),
        ('Member', '0032_rename_complaint_tbl_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('member_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.tbl_memberadding')),
                ('relative_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Member.tbl_relatives')),
            ],
        ),
    ]