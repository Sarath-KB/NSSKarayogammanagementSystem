# Generated by Django 4.2.1 on 2023-06-16 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0019_rename_proof_name_type_tbl_scholarshipname_proof_name'),
        ('Member', '0018_rename_memeber_name_tbl_monthlycollectionpayment_member_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_scholarshipapply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('document', models.FileField(upload_to='Doc/')),
                ('member_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.tbl_memberadding')),
                ('relative_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Member.tbl_relatives')),
                ('scholarship_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_scholarshipname')),
            ],
        ),
    ]
