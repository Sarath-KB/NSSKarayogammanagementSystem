from django.db import models
from Admin.models import *
# Create your models here.

class tbl_chitty(models.Model):
    chitty_name=models.CharField(max_length=50)
    chitty_details=models.CharField(max_length=50)
    head=models.ForeignKey(tbl_financehead,on_delete=models.CASCADE)
    scheme=models.ForeignKey(tbl_scheme,on_delete=models.CASCADE)

class tbl_addloanname(models.Model):
    loan_name=models.CharField(max_length=50)
    loan_details=models.CharField(max_length=50)
    head=models.ForeignKey(tbl_financehead,on_delete=models.CASCADE)
    loan_type=models.ForeignKey(tbl_loan,on_delete=models.CASCADE)

class tbl_loancalender(models.Model):
    amount=models.CharField(max_length=50)
    startdate=models.DateField(max_length=50)
    enddate=models.DateField(max_length=50)
    no_installment=models.CharField(max_length=50)
    head=models.ForeignKey(tbl_financehead,on_delete=models.CASCADE)
    loan_name=models.ForeignKey(tbl_addloanname,on_delete=models.CASCADE)

class tbl_chittycalender(models.Model):
    amount=models.CharField(max_length=50)
    startdate=models.DateField(max_length=50)
    enddate=models.DateField(max_length=50)
    no_installment=models.CharField(max_length=50)
    head=models.ForeignKey(tbl_financehead,on_delete=models.CASCADE)
    chitty_name=models.ForeignKey(tbl_chitty,on_delete=models.CASCADE)

class tbl_weeklycollection(models.Model):
    head=models.ForeignKey(tbl_financehead,on_delete=models.CASCADE)
    amount=models.CharField(max_length=50)

class tbl_monthlycollection(models.Model):
    head=models.ForeignKey(tbl_financehead,on_delete=models.CASCADE)
    amount=models.CharField(max_length=50)