from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)
class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)
class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)
class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_memberadding(models.Model):
    member_name=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    gender=models.CharField(max_length=50)
    photo=models.FileField(upload_to='doc/')
    password=models.CharField(max_length=50,default=1234)
    inactive=models.IntegerField(default=0)

class tbl_financehead(models.Model):
    head_name=models.CharField(max_length=50)
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    fdate=models.DateField(max_length=50)
    tdate=models.DateField(max_length=50)

class tbl_scheme(models.Model):
    scheme_name=models.CharField(max_length=50)

class tbl_loan(models.Model):
    loan_name=models.CharField(max_length=50)

class tbl_proof(models.Model):
    proof_name=models.CharField(max_length=50)

class tbl_relationtype(models.Model):
    relation_type=models.CharField(max_length=50)

class tbl_scholarshiptype(models.Model):
    scholarship_type=models.CharField(max_length=50)

class tbl_scholarshipname(models.Model):
    scholarship_name=models.CharField(max_length=50)
    scholarship_details=models.CharField(max_length=50)
    scholarship_type=models.ForeignKey(tbl_scholarshiptype,on_delete=models.CASCADE)
    proof_name=models.ForeignKey(tbl_proof,on_delete=models.CASCADE)

class tbl_electionposition(models.Model):
    election_position=models.CharField(max_length=50)

class tbl_electiondeclaration(models.Model):
    title=models.CharField(max_length=50)
    details=models.CharField(max_length=200)
    nomination_date=models.DateField(max_length=50)
    verified_date=models.DateField(max_length=50)
    election_date=models.DateField(max_length=50)
    result_date=models.DateField(max_length=50)
    posting_date=models.DateField(auto_now_add=True)
    status=models.IntegerField(default=0)

class tbl_events(models.Model):
    name=models.CharField(max_length=50)
    details=models.CharField(max_length=200)
    event_date=models.DateField(max_length=50)

class tbl_adminlogin(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

