# Generated by Django 4.2.1 on 2023-06-20 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0023_alter_tbl_memberadding_password'),
        ('Member', '0022_tbl_relatives_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_chittyjoin',
            name='memberdata',
        ),
        migrations.AddField(
            model_name='tbl_chittyjoin',
            name='member_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.tbl_memberadding'),
        ),
        migrations.AddField(
            model_name='tbl_chittyjoin',
            name='relative',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Member.tbl_relatives'),
        ),
    ]
