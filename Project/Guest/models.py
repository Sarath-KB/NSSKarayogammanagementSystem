from django.db import models
from Admin.models import *
# Create your models here.
class tbl_newuser(models.Model):
    user_name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    gender=models.CharField(max_length=50)
    photo=models.FileField(upload_to='Doc')
    password=models.CharField(max_length=50)
