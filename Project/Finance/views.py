from django.shortcuts import render,redirect
from Admin.models import *
from Finance.models import *
from Member.models import *

# Create your views here.
def homepage(request):
    if 'fhid' in request.session:
        lcount=tbl_addloanname.objects.all().count()
        ccount=tbl_chitty.objects.all().count()
        return render(request,"Finance/homepage.html",{'lcount':lcount,'ccount':ccount})
    else:
        return redirect("Guest:login")
def myprofile(request):
    if 'fhid' in request.session:
        data=tbl_financehead.objects.get(id=request.session["fhid"])
        return render(request,"Finance/myprofile.html",{'data':data})
    else:
        return redirect("Guest:login")

def editprofile(request):
    
    data=tbl_financehead.objects.get(id=request.session["fhid"])
    if request.method=="POST":
        data.head_name=request.POST.get('txt_name')
        data.user_name=request.POST.get('txt_username')
        
        data.save()
        return redirect("Finance:myprofile")
    else:
        return render(request,"Finance/editprofile.html",{'data':data})

def chitty(request):
    if 'fhid' in request.session:
        schemedata=tbl_scheme.objects.all()
        chittydata=tbl_chitty.objects.all()
        if request.method=="POST":
            headdata=tbl_financehead.objects.get(id=request.session["fhid"])
            sdata=tbl_scheme.objects.get(id=request.POST.get('scheme'))
            tbl_chitty.objects.create(chitty_name=request.POST.get('txt_name'),
            chitty_details=request.POST.get('details'),head=headdata,scheme=sdata)
            return redirect("Finance:chitty")
        else:
            return render(request,"Finance/chitty.html",{'scheme':schemedata,'chitty':chittydata})
    else:
        return redirect("Guest:login")


def deletechitty(request,cid):
    tbl_chitty.objects.get(id=cid).delete()
    return redirect("Finance:chitty")

def chittyapplications(request):
    if 'fhid' in request.session:
        mdata=tbl_memberadding.objects.all()
        rdata=tbl_relatives.objects.all()
    #appdata=tbl_chittyjoin.objects.all()
    #appdata=tbl_chittyjoin.objects.filter(status=0)    
    #appdata=tbl_chittyjoin.objects.filter(status=0)
        mappdata=tbl_chittyjoin.objects.filter(memberdata__in=mdata,status=0)|tbl_chittyjoin.objects.filter(memberdata__in=mdata,status=0)
        rappdata=tbl_chittyjoin.objects.filter(relative__in=rdata,status=0)|tbl_chittyjoin.objects.filter(relative__in=rdata,status=0)
        return render(request,"Finance/viewmemberapplication.html",{'data':mappdata,'data1':rappdata})
    else:
        return redirect("Guest:login")

def chittyaccept(request,amid):
    acceptdata=tbl_chittyjoin.objects.get(id=amid)
    acceptdata.status=1
    acceptdata.save()
    return redirect("Finance:chittyapplications")

def chittyreject(request,rmid):
    rejectdata=tbl_chittyjoin.objects.get(id=rmid)
    rejectdata.status=2
    rejectdata.save()
    return redirect("Finance:chittyapplications")

def chittyacceptlist(request):
    if 'fhid' in request.session:
    #acceptlistdata=tbl_chittyjoin.objects.filter(status=1)
    #return render(request,"Finance/chittyacceptlist.html",{'acceptlist':acceptlistdata})
    #acceptlistdata=tbl_chittyjoin.objects.filter(status=1) |tbl_chittyjoin.objects.filter(status__gt=2)
        mdata=tbl_memberadding.objects.all()
        rdata=tbl_relatives.objects.all()
        mappdata=tbl_chittyjoin.objects.filter(memberdata__in=mdata,status=1)|tbl_chittyjoin.objects.filter(memberdata__in=mdata,status=3)
        rappdata=tbl_chittyjoin.objects.filter(relative__in=rdata,status=1)|tbl_chittyjoin.objects.filter(relative__in=rdata,status=3)
        return render(request,"Finance/chittyacceptlist.html",{'acceptlist':mappdata,'acceptlist1':rappdata})
    else:
        return redirect("Guest:login")

def chittyrejectlist(request):
    if 'fhid' in request.session:
        mdata=tbl_memberadding.objects.all()
        rdata=tbl_relatives.objects.all()
    #rejectlistdata=tbl_chittyjoin.objects.filter(status=2)
        mappdata=tbl_chittyjoin.objects.filter(memberdata__in=mdata,status=2)|tbl_chittyjoin.objects.filter(memberdata__in=mdata,status=2)
        rappdata=tbl_chittyjoin.objects.filter(relative__in=rdata,status=2)|tbl_chittyjoin.objects.filter(relative__in=rdata,status=2)
        return render(request,"Finance/chittyrejectlist.html",{'rejectlist':mappdata,'rejectlist1':rappdata})
    else:
        return redirect("Guest:login")

def addloan(request):
    if 'fhid' in request.session:
        loandata=tbl_loan.objects.all()
        loannamedata=tbl_addloanname.objects.all()
        if request.method=="POST":
            headdata=tbl_financehead.objects.get(id=request.session["fhid"])
            ldata=tbl_loan.objects.get(id=request.POST.get('loan_type'))
            tbl_addloanname.objects.create(loan_name=request.POST.get('txt_name'),
            loan_details=request.POST.get('details'),head=headdata,loan_type=ldata)
            return redirect("Finance:addloan")
        else:
            return render(request,"Finance/addloan.html",{'loan':loandata,'loanname':loannamedata})
    else:
        return redirect("Guest:login")

def deleteloanname(request,lnid):
    if 'fhid' in request.session:
        tbl_addloanname.objects.get(id=lnid).delete()
        return redirect("Finance:addloan")
    else:
        return redirect("Guest:login")

def viewloanapplications(request):
    if 'fhid' in request.session:
        loandata=tbl_loanapply.objects.filter(status=0)
    
        return render(request,"Finance/viewloanapplications.html",{'data':loandata})
    else:
        return redirect("Guest:login")
    
def loanaccept(request,alid):
    acceptdata=tbl_loanapply.objects.get(id=alid)
    acceptdata.status=1
    acceptdata.save()
    return redirect("Finance:viewloanapplications")

def loanreject(request,rlid):
    rejectdata=tbl_loanapply.objects.get(id=rlid)
    rejectdata.status=2
    rejectdata.save()
    return redirect("Finance:viewloanapplications")

def loanrejectlist(request):
    if 'fhid' in request.session:
        rejectlistdata=tbl_loanapply.objects.filter(status=2)
        return render(request,"Finance/loanrejectlist.html",{'rejectlist':rejectlistdata})
    else:
        return redirect("Guest:login")
    

def loanacceptlist(request):
    if 'fhid' in request.session:
        acceptlistdata=tbl_loanapply.objects.filter(status=1) |tbl_loanapply.objects.filter(status__gt=2)
        return render(request,"Finance/loanacceptlist.html",{'acceptlist':acceptlistdata})
    else:
        return redirect("Guest:login")

def chittyview(request,cid):
    data=tbl_chittyjoin.objects.get(id=cid)
    appdata=tbl_chittyjoin.objects.all()
    
    return render(request,"Finance/viewmemberapplication.html",{'data':data})

def loancalender(request,lid):
    if 'fhid' in request.session:
        data=tbl_loancalender.objects.all()
        if request.method=="POST":
            headdata=tbl_financehead.objects.get(id=request.session["fhid"])
            loanname=tbl_addloanname.objects.get(id=lid)
            tbl_loancalender.objects.create(amount=request.POST.get('txt_rs'),
            no_installment=request.POST.get('txt_in'),
            startdate=request.POST.get('sdate'),
            enddate=request.POST.get('edate'),head=headdata,loan_name=loanname)
            return redirect("Finance:addloan")
        else:

            return render(request,"Finance/loancalender.html",{'data':data})
    else:
        return redirect("Guest:login")

def loangrant(request,lgid):
    acceptdata=tbl_loanapply.objects.get(id=lgid)
    acceptdata.status=3
    acceptdata.save()
    return redirect("Finance:homepage")

def viewloanrepay(request,lid):
    if 'fhid' in request.session:
        loanapp=tbl_loanapply.objects.get(id=lid)
        datacount=tbl_repaymentloan.objects.filter(loanapply=loanapp).count()
        loannames=loanapp.loan_name.id
        loancalender=tbl_loancalender.objects.get(loan_name=loannames)
        installments=int(loancalender.no_installment)
        array=[i for i in range(1,installments+1)]
        return render(request,"Finance/ViewRepayment.html",{'data':datacount,'paynumber':loancalender,'array':array})
    else:
        return redirect("Guest:login")

def chittycalender(request,cid):
    if 'fhid' in request.session:
        data=tbl_chittycalender.objects.all()
        if request.method=="POST":
            headdata=tbl_financehead.objects.get(id=request.session["fhid"])
            chittyname=tbl_chitty.objects.get(id=cid)
            tbl_chittycalender.objects.create(amount=request.POST.get('txt_rs'),
            no_installment=request.POST.get('txt_in'),
            startdate=request.POST.get('sdate'),
            enddate=request.POST.get('edate'),head=headdata,chitty_name=chittyname)
            return redirect("Finance:chitty")
        else:
            return render(request,"Finance/chittycalender.html",{'data':data})
    else:
        return redirect("Guest:login")

def deleteloancalender(request,lid):
    tbl_loancalender.objects.get(id=lid).delete()
    return redirect("Admin:loancalender")

def deletechittycalender(request,cid):
    tbl_chittycalender.objects.get(id=cid).delete()
    return redirect("Admin:chittycalender")

def chittygrant(request,cgid):
    acceptdata=tbl_chittyjoin.objects.get(id=cgid)
    acceptdata.status=3
    acceptdata.save()
    return redirect("Finance:homepage")

def viewchittypay(request,cid):
    if 'fhid' in request.session:
        chittyapp=tbl_chittyjoin.objects.get(id=cid)
        datacount=tbl_paymentchitty.objects.filter(chitty_apply=chittyapp).count()
        chittyname=chittyapp.chittydata.id
        chittycalender=tbl_chittycalender.objects.get(chitty_name=chittyname)
        installments=int(chittycalender.no_installment)
        array=[i for i in range(1,installments+1)]
        return render(request,"Finance/viewchittypayment.html",{'data':datacount,'paynumber':chittycalender,'array':array})
    else:
        return redirect("Guest:login")

def weeklycollection(request):
    if 'fhid' in request.session:
        data=tbl_weeklycollection.objects.all()
        if request.method=="POST":
            headdata=tbl_financehead.objects.get(id=request.session["fhid"])
       
            tbl_weeklycollection.objects.create(amount=request.POST.get('txt_amount'),
            head=headdata)
            return redirect("Finance:weeklycollection")
        else:
            return render(request,"Finance/weeklycollection.html",{'data':data})
    else:
        return redirect("Guest:login")


def monthlycollection(request):
    if 'fhid' in request.session:
        data=tbl_monthlycollection.objects.all()
        if request.method=="POST":
            headdata=tbl_financehead.objects.get(id=request.session["fhid"])
       
            tbl_monthlycollection.objects.create(amount=request.POST.get('txt_amount'),
            head=headdata)
            return redirect("Finance:monthlycollection")
        else:
            return render(request,"Finance/monthlycollection.html",{'data':data})
    else:
        return redirect("Guest:login")

def deletemonthlycollection(request,mid):
    tbl_monthlycollection.objects.get(id=mid).delete()
    return redirect("Finance:monthlycollection")

def deleteweeklycollection(request,wid):
    tbl_weeklycollection.objects.get(id=wid).delete()
    return redirect("Finance:weeklycollection")

def scholarshipacceptlist(request):
    if 'fhid' in request.session:
        mdata=tbl_memberadding.objects.all()
        rdata=tbl_relatives.objects.all()
        mappdata=tbl_scholarshipapply.objects.filter(member_name__in=mdata,status=1)|tbl_scholarshipapply.objects.filter(member_name__in=mdata,status=3)
        rappdata=tbl_scholarshipapply.objects.filter(relative_name__in=rdata,status=1)|tbl_scholarshipapply.objects.filter(relative_name__in=rdata,status=3)
   
        return render(request,"Finance/scholarshipaccept.html",{'acceptlist':mappdata,
        'acceptlist1':rappdata})
    else:
        return redirect("Guest:login")

def scholarshipgrant(request,sgid):
    acceptdata=tbl_scholarshipapply.objects.get(id=sgid)
    acceptdata.status=3
    acceptdata.save()
    return redirect("Finance:homepage")

def viewweeklycollectionpayment(request):
    if 'fhid' in request.session:
        rdata=tbl_relatives.objects.all()
        data=tbl_weeklycollectionpayment.objects.all()
    #datacount=tbl_weeklycollectionpayment.objects.filter(relative_name=rdata).count
    #dcount=tbl_weeklycollectionpayment.objects.filter(weeklycollection_id=datacount)
    
        return render(request,"Finance/viewweeklycollectionpayment.html",{'data':data})
    else:
        return redirect("Guest:login")

def viewmonthlycollectionpayment(request):
    if 'fhid' in request.session:
    #rdata=tbl_relatives.objects.all()
        data=tbl_monthlycollectionpayment.objects.all()
    #datacount=tbl_weeklycollectionpayment.objects.filter(relative_name=rdata).count
    #dcount=tbl_weeklycollectionpayment.objects.filter(weeklycollection_id=datacount)
    
        return render(request,"Finance/viewmonthlycollectionpayment.html",{'data':data})
    else:
        return redirect("Guest:login")

def logout(request):
    if 'fhid' in request.session:
        del request.session["fhid"]
        return redirect("Guest:login")
    else:
        #del request.session["reid"]
        return redirect("Guest:login")

def changepassword(request):
    if request.method=="POST":
        fcount=tbl_financehead.objects.filter(id=request.session["fhid"],
        password=request.POST.get("oldpass")).count()
        if fcount>0:
            if request.POST.get('newpass')==request.POST.get('conpass'):
                fdata=tbl_financehead.objects.get(id=request.session["fhid"])
                fdata.password=request.POST.get('newpass')
                fdata.save()
                return redirect("Finance:homepage")
            else:
                return render(request,"Finance/changepassword.html")
        else:
            return render(request,"Finance/changepassword.html")
    else:
        return render(request,"Finance/changepassword.html")

def chittyreport(request,cid):
    data=tbl_chitty.objects.get(id=cid)
    mdata=tbl_memberadding.objects.all()
    rdata=tbl_relatives.objects.all()
    if request.method=="POST":
        if request.POST.get('fdate')!="" and request.POST.get('edate'):
            datas=tbl_chittyjoin.objects.filter(chittydata=data,memberdata__in=mdata,status=3,apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
            data=tbl_chittyjoin.objects.filter(chittydata=data,relative__in=rdata,status=3,apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
            return render(request,"Finance/chittyreport.html",{'data':datas,'data1':data})
        elif request.POST.get('fdate')!="":
            datas=tbl_chittyjoin.objects.filter(chittydata=data,memberdata__in=mdata,status=3,apply_date__gte=request.POST.get('fdate'))
            data=tbl_chittyjoin.objects.filter(chittydata=data,relative__in=rdata,status=3,apply_date__gte=request.POST.get('fdate'))
            return render(request,"Finance/chittyreport.html",{'data':datas,'data1':data})
        else:
            datas=tbl_chittyjoin.objects.filter(chittydata=data,status=3,memberdata__in=mdata,apply_date__lte=request.POST.get('edate'))
            data=tbl_chittyjoin.objects.filter(chittydata=data,status=3,relative__in=rdata,apply_date__lte=request.POST.get('edate'))
            return render(request,"Finance/chittyreport.html",{'data':datas,'data1':data})
    else:
        return render(request,"Finance/chittyreport.html")

def loanreport(request,lid):
    data=tbl_addloanname.objects.get(id=lid)
    if request.method=="POST":
        if request.POST.get('fdate')!="" and request.POST.get('edate'):
            datas=tbl_loanapply.objects.filter(loan_name=data,status=3,apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
            return render(request,"Finance/loanreport.html",{'data':datas})
        elif request.POST.get('fdate')!="":
            datas=tbl_loanapply.objects.filter(loan_name=data,status=3,apply_date__gte=request.POST.get('fdate'))
            return render(request,"Finance/loanreport.html",{'data':datas})
        else:
            datas=tbl_loanapply.objects.filter(loan_name=data,status=3,apply_date__lte=request.POST.get('edate'))
            return render(request,"Finance/loanreport.html",{'data':datas})
    else:
        return render(request,"Finance/loanreport.html")

def chittyfunding(request):
    if 'fhid' in request.session:
        mdata=tbl_memberadding.objects.all()
        rdata=tbl_relatives.objects.all()
        mappdata=tbl_chittyfunding.objects.filter(member_name__in=mdata,status=0)|tbl_chittyfunding.objects.filter(member_name__in=mdata,status=0)
        rappdata=tbl_chittyfunding.objects.filter(relative_name__in=rdata,status=0)|tbl_chittyfunding.objects.filter(relative_name__in=rdata,status=0)
        return render(request,"Finance/viewchittyfundingapplication.html",{'data':mappdata,'data1':rappdata})
    else:
        return redirect("Guest:login")

def chittyfundingaccept(request,cfid):
    acceptdata=tbl_chittyfunding.objects.get(id=cfid)
    acceptdata.status=1
    acceptdata.save()
    return redirect("Finance:chittyfunding")

def chittyfundingreject(request,rcfid):
    rejectdata=tbl_chittyfunding.objects.get(id=rcfid)
    rejectdata.status=2
    rejectdata.save()
    return redirect("Finance:chittyfunding")

def chittyfundingacceptlist(request):
    if 'fhid' in request.session:
        mdata=tbl_memberadding.objects.all()
        rdata=tbl_relatives.objects.all()
        mappdata=tbl_chittyfunding.objects.filter(member_name__in=mdata,status=1)|tbl_chittyfunding.objects.filter(member_name__in=mdata,status=3)
        rappdata=tbl_chittyfunding.objects.filter(relative_name__in=rdata,status=1)|tbl_chittyfunding.objects.filter(relative_name__in=rdata,status=3)
        return render(request,"Finance/chittyfundingacceptlist.html",{'status':mappdata,'status1':rappdata})
    else:
        return redirect("Guest:login")

def chittyfundinggrant(request,cfgid):
    acceptdata=tbl_chittyfunding.objects.get(id=cfgid)
    acceptdata.status=3
    acceptdata.save()
    return redirect("Finance:homepage")

def viewcomplaint(request):
    if 'fhid' in request.session:
        mdata=tbl_memberadding.objects.all()
        rdata=tbl_relatives.objects.all()
        mappdata=tbl_complaint.objects.filter(member_name__in=mdata)|tbl_complaint.objects.filter(member_name__in=mdata)
        rappdata=tbl_complaint.objects.filter(relative_name__in=rdata)|tbl_complaint.objects.filter(relative_name__in=rdata)
        return render(request,"Finance/viewcomplaint.html",{'data':mappdata,'data1':rappdata})
    else:
        return redirect("Guest:login")

def viewfeedback(request):
    if 'fhid' in request.session:
        mdata=tbl_memberadding.objects.all()
        rdata=tbl_relatives.objects.all()
        mappdata=tbl_feedback.objects.filter(member_name__in=mdata)|tbl_feedback.objects.filter(member_name__in=mdata)
        rappdata=tbl_feedback.objects.filter(relative_name__in=rdata)|tbl_feedback.objects.filter(relative_name__in=rdata)
        return render(request,"Finance/viewfeedback.html",{'data':mappdata,'data1':rappdata})
    else:
        return redirect("Guest:login")

def complaintreply(request,cid):
    if 'fhid' in request.session:
        data=tbl_complaint.objects.get(id=cid)
        if request.method=="POST":
            rdata=request.POST.get('txt_reply')
            data.reply=rdata
            data.status=1
            #data.reply_date=date.today()
            data.save()
            return redirect("Finance:homepage")
        else:
            return render(request,"Finance/complaintreply.html")
    else:
        return redirect("Guest:login")
        #return render(request,"Finance/complaintreply.html")



     