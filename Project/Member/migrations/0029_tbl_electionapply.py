# Generated by Django 4.2.1 on 2023-06-21 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0030_tbl_electiondeclaration'),
        ('Member', '0028_tbl_paymentchitty'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_electionapply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('election_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_electiondeclaration')),
                ('election_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_electionposition')),
                ('member_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_memberadding')),
            ],
        ),
    ]
