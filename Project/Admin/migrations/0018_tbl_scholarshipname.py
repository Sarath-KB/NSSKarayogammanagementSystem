# Generated by Django 4.2.1 on 2023-06-15 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0017_tbl_scholarshiptype'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_scholarshipname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scholarship_name', models.CharField(max_length=50)),
                ('scholarship_details', models.CharField(max_length=50)),
                ('proof_name_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_proof')),
                ('scholarship_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_scholarshiptype')),
            ],
        ),
    ]
