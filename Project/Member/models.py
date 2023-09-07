from django.db import models
from Finance.models import *
from Admin.models import *
from Member.models import *

# Create your models here.

class tbl_chittyjoin(models.Model):
    status=models.IntegerField(default=0)
    document=models.FileField(upload_to='Doc/')
    chittydata=models.ForeignKey(tbl_chitty,on_delete=models.CASCADE)
    #memberdata=models.ForeignKey(tbl_memberadding,on_delete=models.CASCADE)
    proof_name=models.ForeignKey(tbl_proof,on_delete=models.CASCADE)
    memberdata=models.ForeignKey(tbl_memberadding,on_delete=models.SET_NULL,null=True)
    relative=models.ForeignKey("Member.tbl_relatives",on_delete=models.SET_NULL,null=True)
    apply_date=models.DateField(auto_now_add=True)

class tbl_loanapply(models.Model):
    status=models.IntegerField(default=0)
    document=models.FileField(upload_to='Doc/')
    loan_name=models.ForeignKey(tbl_addloanname,on_delete=models.CASCADE)
    member_name=models.ForeignKey(tbl_memberadding,on_delete=models.CASCADE)
    proof_name=models.ForeignKey(tbl_proof,on_delete=models.CASCADE)
    apply_date=models.DateField(auto_now_add=True)

class tbl_repaymentloan(models.Model):
    loanapply=models.ForeignKey(tbl_loanapply,on_delete=models.CASCADE)
    member=models.ForeignKey(tbl_memberadding,on_delete=models.CASCADE)
    repayment_date=models.DateField(auto_now_add=True)


class tbl_paymentchitty(models.Model):
    chitty_apply=models.ForeignKey(tbl_chittyjoin,on_delete=models.CASCADE)
    #member=models.ForeignKey(tbl_memberadding,on_delete=models.CASCADE)
    memberdata=models.ForeignKey(tbl_memberadding,on_delete=models.SET_NULL,null=True)
    relative=models.ForeignKey("Member.tbl_relatives",on_delete=models.SET_NULL,null=True)
    repayment_date=models.DateField(auto_now_add=True)

class tbl_relatives(models.Model):
    relative_name=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    photo=models.FileField(upload_to='doc/')
    member_name=models.ForeignKey(tbl_memberadding,on_delete=models.CASCADE)
    relation_type=models.ForeignKey(tbl_relationtype,on_delete=models.CASCADE)
    refer_id=models.IntegerField()
    password=models.CharField(max_length=50,default=1234)
    inactive=models.IntegerField(default=0)
    address=models.CharField(max_length=100)


class tbl_weeklycollectionpayment(models.Model):
    #relative_name=models.ForeignKey(tbl_relatives,on_delete=models.CASCADE)
    weeklycollection_id=models.ForeignKey(tbl_weeklycollection,on_delete=models.CASCADE,null=True)
    member_name=models.ForeignKey(tbl_memberadding,on_delete=models.SET_NULL,null=True)
    relative_name=models.ForeignKey(tbl_relatives,on_delete=models.SET_NULL,null=True)
    payment_date=models.DateField(auto_now_add=True)


class tbl_monthlycollectionpayment(models.Model):
    member_name=models.ForeignKey(tbl_memberadding,on_delete=models.CASCADE)
    monthlycollection_id=models.ForeignKey(tbl_monthlycollection,on_delete=models.CASCADE)
    payment_date=models.DateField(auto_now_add=True)


class tbl_scholarshipapply(models.Model):
    status=models.IntegerField(default=0)
    document=models.FileField(upload_to='Doc/')
    scholarship_name=models.ForeignKey(tbl_scholarshipname,on_delete=models.CASCADE)
    member_name=models.ForeignKey(tbl_memberadding,on_delete=models.SET_NULL,null=True)
    relative_name=models.ForeignKey(tbl_relatives,on_delete=models.SET_NULL,null=True)
    apply_date=models.DateField(auto_now_add=True)

class tbl_electionapply(models.Model):
    status=models.IntegerField(default=0)
    election_name=models.ForeignKey(tbl_electiondeclaration,on_delete=models.CASCADE)
    member_name=models.ForeignKey(tbl_memberadding,on_delete=models.CASCADE)
    election_position=models.ForeignKey(tbl_electionposition,on_delete=models.CASCADE)

class tbl_voting(models.Model):
    election_apply=models.ForeignKey(tbl_electionapply,on_delete=models.CASCADE)
    member_name=models.ForeignKey(tbl_memberadding,on_delete=models.SET_NULL,null=True)
    relative_name=models.ForeignKey(tbl_relatives,on_delete=models.SET_NULL,null=True)

class tbl_complaint(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=200)
    member_name=models.ForeignKey(tbl_memberadding,on_delete=models.SET_NULL,null=True)
    relative_name=models.ForeignKey(tbl_relatives,on_delete=models.SET_NULL,null=True)
    reply=models.CharField(max_length=200,default="Not viewed")
    status=models.IntegerField(default=0)

class tbl_feedback(models.Model):
    content=models.CharField(max_length=200)
    member_name=models.ForeignKey(tbl_memberadding,on_delete=models.SET_NULL,null=True)
    relative_name=models.ForeignKey(tbl_relatives,on_delete=models.SET_NULL,null=True)

class tbl_chittyfunding(models.Model):
    chitty_name=models.ForeignKey(tbl_chitty,on_delete=models.CASCADE)
    document=models.FileField(upload_to='Doc/')
    member_name=models.ForeignKey(tbl_memberadding,on_delete=models.SET_NULL,null=True)
    relative_name=models.ForeignKey(tbl_relatives,on_delete=models.SET_NULL,null=True)
    status=models.IntegerField(default=0)
    proof_name=models.ForeignKey(tbl_proof,on_delete=models.CASCADE)



    
