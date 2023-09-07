from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Member.models import *
from django.core.mail import send_mail
from django.conf import settings
import random
# Create your views here.
def newuser(request):
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        pla=tbl_place.objects.get(id=request.POST.get('place'))
        tbl_newuser.objects.create(user_name=request.POST.get('txt_name'),
        contact=request.POST.get('txt_contact'),
        email=request.POST.get('txt_email'),
        address=request.POST.get('txt_address'),
        photo=request.FILES.get('photo'),
        password=request.POST.get('pass'),
        gender=request.POST.get('gender'),place=pla)
        return render(request,"Guest/Newuser.html",{'district':districtdata})
    else:
        return render(request,"Guest/Newuser.html",{'district':districtdata})

def ajaxplace(request):
    districtdata=tbl_district.objects.get(id=request.GET.get('disd'))
    placedata=tbl_place.objects.filter(district=districtdata)
    return render(request,"Guest/Ajaxplace.html",{'place':placedata})

def login(request):
    if request.method=="POST":
        passw="12345678"
        membercount=tbl_memberadding.objects.filter(email=request.POST.get('txt_username'),
        password=request.POST.get('pass')).count()
        financecount=tbl_financehead.objects.filter(user_name=request.POST.get('txt_username'),
        password=request.POST.get('pass')).count()
        relativecount=tbl_relatives.objects.filter(email=request.POST.get('txt_username'),inactive__lt=2).count()
        relativecount1=tbl_relatives.objects.filter(email=request.POST.get('txt_username'),inactive=2).count()
        admincount=tbl_adminlogin.objects.filter(email=request.POST.get('txt_username'),password=request.POST.get('pass')).count()
        if membercount>0:
            memberdata=tbl_memberadding.objects.get(email=request.POST.get('txt_username'),
            password=request.POST.get('pass'))
            request.session["mid"]=memberdata.id
            return redirect("Member:homepage")
        elif financecount>0:
            financedata=tbl_financehead.objects.get(user_name=request.POST.get('txt_username'),
            password=request.POST.get('pass'))
            request.session["fhid"]=financedata.id
            return redirect("Finance:homepage")
        elif relativecount>0:
            relativedata=tbl_relatives.objects.get(email=request.POST.get('txt_username'))
            request.session["reid"]=relativedata.id
            return redirect("Member:homepage")
        elif relativecount1>0:
            rem=1
            return redirect("Guest:login")    
        elif admincount>0:
            admindata=tbl_adminlogin.objects.get(email=request.POST.get('txt_username'),password=request.POST.get('pass'))
            request.session["aid"]=admindata.id
            return redirect("Admin:homepage")
        else:
            return render(request,"Guest/login.html",{'mess':1})
    else:
        return render(request,"Guest/login.html")

def index(request):
    return render(request,"Guest/index.html")

def ForgetPassword(request):
    
    if request.method=="POST":
        otp=random.randint(10000, 999999)
        request.session["otp"]=otp
        request.session["femail"]=request.POST.get('txtemail')
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rYour OTP for reset password is "+str(otp),#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txtemail')],
        )
        return redirect("Guest:verification")
    else:
        return render(request,"Guest/forgetpassword.html")

def OtpVerification(request):
    if request.method=="POST":
        otp=int(request.session["otp"])
        if int(request.POST.get('txtotp'))==otp:
            return redirect("Guest:create")
    return render(request,"Guest/OTPverification.html")



def CreateNewPass(request):
    if request.method=="POST":
        if request.POST.get('txtpassword2')==request.POST.get('txtpassword3'):
            membercount=tbl_memberadding.objects.filter(email=request.session["femail"]).count()
            relativecount=tbl_relatives.objects.filter(email=request.session["femail"]).count()
            financecount=tbl_financehead.objects.filter(user_name=request.session["femail"]).count()
            #hospitalcount=tbl_newhospital.objects.filter(email=request.session["femail"]).count()
            if membercount>0:
                member=tbl_memberadding.objects.get(email=request.session["femail"])
                member.password=request.POST.get('txtpassword2')
                member.save()
                return redirect("Guest:login")

            elif relativecount>0:
                relative=tbl_relatives.objects.get(email=request.session["femail"])
                relative.password=request.POST.get('txtpassword2')
                relative.save()
                return redirect("Guest:login")

            else:
                finance=tbl_financehead.objects.get(user_name=request.session["femail"])
                finance.password=request.POST.get('txtpassword2')
                finance.save()
                return redirect("Guest:login")

            # else:
            #     hos=tbl_new.objects.get(email=request.session["femail"])
            #     hos.tbl_newhospital=request.POST.get('txtpassword2')
            #     hos.save()
            #     return redirect("Guest:login")
    else:       
        return render(request,"Guest/createnewpassword.html")



def ajaxemail(request):
    membercount=tbl_memberadding.objects.filter(email=request.GET.get("email")).count()
    financeheadcount=tbl_relatives.objects.filter(email=request.GET.get("email")).count()
    relativecount=tbl_financehead.objects.filter(user_name=request.GET.get("email")).count()
    admincount=tbl_adminlogin.objects.filter(email=request.GET.get("email")).count()
    if membercount>0 or financeheadcount>0 or relativecount>0 or admincount>0:
        return render(request,"Guest/Ajaxemail.html",{'mess':1})
    else:
         return render(request,"Guest/Ajaxemail.html")

   