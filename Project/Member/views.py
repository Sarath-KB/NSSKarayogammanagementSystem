from django.shortcuts import render,redirect
from Admin.models import *
from Finance.models import *
from Member.models import *
from datetime import date,timedelta,datetime
from dateutil.relativedelta import relativedelta

def add_months_with_year_change(start_date, n_months):
    result_dates = []
    current_date = start_date

    for _ in range(n_months):
        # Add one month to the current date using relativedelta
        current_date += relativedelta(months=1)

        # Append the current date to the array
        result_dates.append(current_date)
    #print(result_dates)
    return result_dates
# Create your views here.

def add_months(start_date, n):
    month = start_date.month - 1 + n
    year = start_date.year + month // 12
    month = month % 12 + 1
    day = min(start_date.day, (start_date.replace(year=year, month=month + 1, day=1) - timedelta(days=1)).day)
    return start_date.replace(year=year, month=month, day=day)

def myprofile(request):
    if 'mid' in request.session:
        data=tbl_memberadding.objects.get(id=request.session["mid"])
        return render(request,"Member/myprofile.html",{'data1':data})
    elif 'reid' in request.session:
        data=tbl_relatives.objects.get(id=request.session["reid"])
        return render(request,"Member/myprofile.html",{'data':data})
    else:
        return redirect("Guest:login")

def homepage(request):
    sdata=tbl_scholarshipname.objects.all().count()
    cdata=tbl_chitty.objects.all().count()
    ldata=tbl_addloanname.objects.all().count()
    #return render(request,"Member/homepage.html",{'data3':data3})
    cdate=date.today()
    datacount=tbl_electiondeclaration.objects.filter(result_date__gte=cdate).count()
    edatacount=tbl_events.objects.filter(event_date__gte=cdate).count()
    # if edatacount>0:
    #     data4=tbl_events.objects.filter(event_date__gte=cdate)
    if datacount>0:
        #data4=tbl_events.objects.filter(event_date__gte=cdate)
        data3=tbl_electiondeclaration.objects.filter(result_date__gte=cdate)
        if 'reid' in request.session:
            data=tbl_relatives.objects.get(id=request.session["reid"])
            
            return render(request,"Member/homepage.html",{'data':data,'data3':data3,'sdata':sdata,'cdata':cdata,'ldata':ldata})
        elif 'mid' in request.session:
            mdata=tbl_memberadding.objects.get(id=request.session["mid"])
            
            return render(request,"Member/homepage.html",{'data1':mdata,'data3':data3})
        else:
            return render(request,"Member/homepage.html",{'sdata':sdata,'cdata':cdata,'ldata':ldata})
    else:
        if 'reid' in request.session:
            data=tbl_relatives.objects.get(id=request.session["reid"])
            
            return render(request,"Member/homepage.html",{'data':data,'sdata':sdata,'cdata':cdata,'ldata':ldata})
        elif 'mid' in request.session:
            mdata=tbl_memberadding.objects.get(id=request.session["mid"])
            return render(request,"Member/homepage.html",{'data1':mdata,'sdata':sdata,'cdata':cdata,'ldata':ldata})
        else:
            return render(request,"Member/homepage.html",{'sdata':sdata,'cdata':cdata,'ldata':ldata})
    
   

def editprofile(request):
    if 'mid' in request.session:
        data=tbl_memberadding.objects.get(id=request.session["mid"])
        if request.method=="POST":
            data.member_name=request.POST.get('txt_name')
            data.age=request.POST.get('txt_age')
            data.contact=request.POST.get('contact')
            data.email=request.POST.get('email')
            data.address=request.POST.get('address')
            data.save()
            return redirect("Member:myprofile")
        else:
            return render(request,"Member/editprofile.html",{'data1':data})

    elif 'reid' in request.session:
        data=tbl_relatives.objects.get(id=request.session["reid"])
        if request.method=="POST":
            data.relative_name=request.POST.get('txt_name')
            data.age=request.POST.get('txt_age')
            data.contact=request.POST.get('contact')
            data.email=request.POST.get('email')
            #data.address=request.POST.get('address')
            data.save()
            return redirect("Member:myprofile")
        else:
            return render(request,"Member/editprofile.html",{'data':data})
    else:
        return render(request,"Member/homepage.html")

def changepassword(request):
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        if request.method=="POST":
            membercount=tbl_memberadding.objects.filter(id=request.session["mid"],
            password=request.POST.get("oldpass")).count()
            if membercount>0:
                if request.POST.get('newpass')==request.POST.get('conpass'):
                    # memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
                    memberdata.password=request.POST.get('newpass')
                    memberdata.save()
                    return redirect("Member:homepage")
                else:
                    return render(request,"Member/changepassword.html",{'data1':memberdata})
            else:
                return render(request,"Member/changepassword.html",{'data1':memberdata})
        else:
            return render(request,"Member/changepassword.html",{'data1':memberdata})
    elif 'reid' in request.session:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        if request.method=="POST":
            rcount=tbl_relatives.objects.filter(id=request.session["reid"],
            password=request.POST.get("oldpass")).count()
            if rcount>0:
                if request.POST.get('newpass')==request.POST.get('conpass'):
                    
                    rdata.password=request.POST.get('newpass')
                    rdata.save()
                    return redirect("Member:homepage")
                else:
                    return render(request,"Member/changepassword.html",{'data':rdata})
            else:
                return render(request,"Member/changepassword.html",{'data':rdata})
        else:
            return render(request,"Member/changepassword.html",{'data':rdata})
    else:
        return redirect("Member:homepage")


def chittyview(request):
    schemedata=tbl_scheme.objects.all()
    chittydata=tbl_chitty.objects.all()
    if 'mid' in request.session:
        mdata=tbl_memberadding.objects.get(id=request.session["mid"])
        return render(request,"Member/chittyview.html",{'chitty':chittydata,'scheme':schemedata,'data1':mdata})
    elif 'reid' in request.session:
        mdata=tbl_relatives.objects.get(id=request.session["reid"])
        return render(request,"Member/chittyview.html",{'chitty':chittydata,'scheme':schemedata,'data':mdata})

def ajaxchitty(request):
    schemedata=tbl_scheme.objects.get(id=request.GET.get('sid'))
    chittydata=tbl_chitty.objects.filter(scheme=schemedata)
    return render(request,"Member/Ajaxscheme.html",{'chitty':chittydata})

def chittyjoin(request,cid):
    prooftype=tbl_proof.objects.all() 
    chittyjoindata=tbl_chittyjoin.objects.all()
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        chittydata=tbl_chitty.objects.get(id=cid)
        if request.method=="POST":
            ptype=tbl_proof.objects.get(id=request.POST.get('ptype'))
            applycount=tbl_chittyjoin.objects.filter(chittydata=chittydata,memberdata=memberdata).count()
            if applycount>0:
                return render(request,"Member/All.html",{'mess2':1})
            else:
                tbl_chittyjoin.objects.create(memberdata=memberdata,chittydata=chittydata,
                proof_name=ptype,document=request.FILES.get('proof'))
                return redirect("Member:homepage")

        else:
            return render(request,"Member/chittyapply.html",{'cdata':chittydata,'ptype':prooftype,'data1':memberdata})
    elif 'reid' in request.session:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        chittydata=tbl_chitty.objects.get(id=cid)
        if request.method=="POST":
            ptype=tbl_proof.objects.get(id=request.POST.get('ptype'))
            applycount=tbl_chittyjoin.objects.filter(chittydata=chittydata,relative=rdata).count()
            if applycount>0:
                return render(request,"Member/All.html",{'mess2':1})
            else:

                tbl_chittyjoin.objects.create(relative=rdata,chittydata=chittydata,
                proof_name=ptype,document=request.FILES.get('proof'))
                return redirect("Member:homepage")
        else:
            return render(request,"Member/chittyapply.html",{'cdata':chittydata,'ptype':prooftype,'data':rdata})
    else:
        return redirect("Member:homepage")

def chittystatusview(request):
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        mdata=tbl_chittyjoin.objects.filter(memberdata=memberdata)
        return render(request,"Member/chittystatusview.html",{'chittystatusview':mdata,'data1':memberdata})
    elif 'reid' in request.session:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        data=tbl_chittyjoin.objects.filter(relative=rdata)
        return render(request,"Member/chittystatusview.html",{'chittystatusview1':data,'data':rdata})
    else:
        return redirect("Member:homepage")

def loanview(request):
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session['mid'])
        loandata=tbl_loan.objects.all()
        loannamedata=tbl_addloanname.objects.all()
        return render(request,"Member/viewloan.html",{'loanname':loannamedata,'loan':loandata,'data1':memberdata})
    else:
        return redirect("Guest:login")

def ajaxloan(request):
    loandata=tbl_loan.objects.get(id=request.GET.get('lid'))
    loannamedata=tbl_addloanname.objects.filter(loan_type=loandata)
    return render(request,"Member/Ajaxloan.html",{'loanname':loannamedata})

def loanapply(request,lnid):
    if 'mid' in request.session:
        cdate=date.today()
        prooftype=tbl_proof.objects.all() 
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        loannamedata=tbl_addloanname.objects.get(id=lnid)
        seldata=tbl_loancalender.objects.get(loan_name=loannamedata)
        sdate=seldata.startdate
        edate=seldata.enddate
        st=0
        if request.method=="POST":
            
            loanapplycount=tbl_loanapply.objects.filter(member_name=memberdata,status__gt=2).count()
            #print(loanapplycount)
            if loanapplycount>0:
            
                loanapplydata=tbl_loanapply.objects.filter(member_name=memberdata,status__gt=2)
                for ap in loanapplydata:
                    lnamedata=tbl_addloanname.objects.get(id=ap.loan_name.id)
                    caldata=tbl_loancalender.objects.get(loan_name=lnamedata)
                    totcount=int(caldata.no_installment)
                    lpdata=tbl_loanapply.objects.get(id=ap.id)
                    repaycount=tbl_repaymentloan.objects.filter(loanapply=lpdata).count()
                    #print(repaycount)
                    if repaycount == totcount:
                        continue
                    else:
                        st=1
                        break
            #print(st)
            if st==1:
                return render(request,"Member/All.html",{'mess':1})
            else:
                if cdate>=sdate and cdate<=edate: 
                    ptype=tbl_proof.objects.get(id=request.POST.get('ptype'))
                    tbl_loanapply.objects.create(member_name=memberdata,loan_name=loannamedata,
                    proof_name=ptype,document=request.FILES.get('proof'))
                    return redirect("Member:homepage")
                else:
                    return redirect("Member:homepage")
        else:
            return render(request,"Member/loanapply.html",{'ldata':loannamedata,'ptype':prooftype,'data1':memberdata})
    else:
        return redirect("Guest:login")

def loanstatusview(request):
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        loandata=tbl_loanapply.objects.filter(member_name=memberdata)
        
        return render(request,"Member/loanstatusview.html",{'loanstatusview':loandata,'data1':memberdata})
    else:
        return redirect("Guest:login")

def loanpay(request,lpid):
    if 'mid' in request.session:
        darray=[]
        cdate=date.today()
        #data=tbl_loancalender.objects.all() 
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        loandata=tbl_addloanname.objects.get(id=lpid)
        payno=tbl_loancalender.objects.get(loan_name=loandata)
        loanapp=tbl_loanapply.objects.get(loan_name=loandata,member_name=memberdata)

        ###########################################################################
        ldate=loanapp.apply_date
        
    
        ###########################################################################
        loanrapycount=tbl_repaymentloan.objects.filter(loanapply=loanapp).count()
        pay=int(payno.no_installment)
        parray=[i for i  in range(1,pay+1)]
        startdate=add_months(ldate,1)
        print(startdate)
        startdate=str(startdate)
        date_object = datetime.strptime(startdate, "%Y-%m-%d")
        resultarray=add_months_with_year_change(date_object,pay)
        for dates in resultarray:
            darray.append(dates.strftime("%Y-%m-%d"))
        print(darray)
        # darray=[]
        # j=0
        # darray.append(startdate)
        # ldate=startdate
        # for i in parray:
        #     ldate=str(ldate)
            # print("First Time:") 
            # print(type(ldate))
            # date_object = datetime.strptime(ldate, "%Y-%m-%d")
            # ldate= date_object
            # print("Second Time:") 
            # print(type(ldate))
            # month = date_object.month
            # if i%12==0:
            #     res=i//12
            #     ldate=add_months(ldate,res)
            #     edate=str(ldate)
            #     darray.append(edate)
            # else:
            #     res=i%12
            #     ldate=add_months(ldate,res)
            #     edate=str(ldate)
            #     darray.append(edate)
            # print("Third Time:") 
            # print(type(ldate))
            #if month>=12:
                #pass
                # j=j+1
                # ldate=add_months(ldate,j)
                # print(type(ldate))
            #else:
            #    pass
                # ldate=add_months(ldate,i)
                # print(type(ldate))

            
                # print(emiadte)
        datas=zip(parray,darray)
        return render(request,"Member/loanpay.html",{'paynumber':payno,'array':datas,'paycount':loanrapycount,'cdate':cdate,'data1':memberdata})
    else:
        return redirect("Guest:login")

def repaymentloan(request,lid):
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        londata=tbl_addloanname.objects.get(id=lid)
        if request.method=="POST":
            loanappdata=tbl_loanapply.objects.get(member_name=memberdata,loan_name=londata)
            tbl_repaymentloan.objects.create(loanapply=loanappdata,member=memberdata)
            return redirect("Member:runpayment")
        else:
            return render(request,"Member/DesignPayment.html")
    else:
        return redirect("Guest:login")

def chittypay(request,cpid):
    #data=tbl_loancalender.objects.all() 
    darray=[]
    cdate=date.today()
    if 'mid' in request.session:

        mdata=tbl_memberadding.objects.get(id=request.session["mid"])
        cdata=tbl_chitty.objects.get(id=cpid)
        payno=tbl_chittycalender.objects.get(chitty_name=cdata)
        chittyapp=tbl_chittyjoin.objects.get(chittydata=cdata,memberdata=mdata)
        chittypaycount=tbl_paymentchitty.objects.filter(chitty_apply=chittyapp).count()
        pay=int(payno.no_installment)
        parray=[i for i  in range(1,pay+1)]
        ldate=chittyapp.apply_date
        startdate=add_months(ldate,1)
        print(startdate)
        startdate=str(startdate)
        date_object = datetime.strptime(startdate, "%Y-%m-%d")
        resultarray=add_months_with_year_change(date_object,pay)
        for dates in resultarray:
            darray.append(dates.strftime("%Y-%m-%d"))
        print(darray)
        datas=zip(parray,darray)
        return render(request,"Member/chittypay.html",{'paynumber':payno,'array':datas,
        'paycount':chittypaycount,'data1':mdata})
    elif 'reid' in request.session:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        cdata=tbl_chitty.objects.get(id=cpid)
        payno=tbl_chittycalender.objects.get(chitty_name=cdata)
        chittyapp=tbl_chittyjoin.objects.get(chittydata=cdata,relative=rdata)
        chittypaycount=tbl_paymentchitty.objects.filter(chitty_apply=chittyapp).count()
        pay=int(payno.no_installment)
        parray=[i for i  in range(1,pay+1)]
        ldate=chittyapp.apply_date
        startdate=add_months(ldate,1)
        print(startdate)
        startdate=str(startdate)
        date_object = datetime.strptime(startdate, "%Y-%m-%d")
        resultarray=add_months_with_year_change(date_object,pay)
        for dates in resultarray:
            darray.append(dates.strftime("%Y-%m-%d"))
        print(darray)
        datas=zip(parray,darray)
        return render(request,"Member/chittypay.html",{'paynumber':payno,'array':datas,
        'paycount':chittypaycount,'data':rdata})
    else:
        return redirect("Member:homepage")

def paymentchitty(request,cid):
    if request.method=="POST":
        if 'mid' in request.session:

            mdata=tbl_memberadding.objects.get(id=request.session["mid"])
            cdata=tbl_chitty.objects.get(id=cid)
            chittyapplydata=tbl_chittyjoin.objects.get(memberdata=mdata,chittydata=cdata)
            tbl_paymentchitty.objects.create(chitty_apply=chittyapplydata,memberdata=mdata)
            return redirect("Member:runpayment")
        elif 'reid' in request.session:
            rdata=tbl_relatives.objects.get(id=request.session["reid"])
            cdata=tbl_chitty.objects.get(id=cid)
            chittyapplydata=tbl_chittyjoin.objects.get(relative=rdata,chittydata=cdata)
            tbl_paymentchitty.objects.create(chitty_apply=chittyapplydata,relative=rdata)
            return redirect("Member:runpayment")
        else:
            return redirect("Member:homepage")
    else:
        return render(request,"Member/DesignPayment.html")

def relatives(request):
    if 'mid' in request.session:
        rtdata=tbl_relationtype.objects.all()
        mdata=tbl_memberadding.objects.get(id=request.session["mid"])
        data=tbl_relatives.objects.filter(member_name=mdata)

        if request.method=="POST":
            rdata=tbl_relationtype.objects.all()

            redata=tbl_relationtype.objects.get(id=request.POST.get('relation'))
            rel=request.POST.get('selr')
            tbl_relatives.objects.create(relative_name=request.POST.get('txt_name'),
            age=request.POST.get('txt_age'),contact=request.POST.get('txt_contact'),
            email=request.POST.get('txt_email'),gender=request.POST.get('gender'),
            address=request.POST.get('txt_address'),
            photo=request.FILES.get('photo'),member_name=mdata,relation_type=redata,refer_id=rel)
            return redirect("Member:relatives")
        else:
            return render(request,"Member/relatives.html",{'relationtype':rtdata,'datas':data,'data1':mdata})
    else:
        return redirect("Guest:login")

def Ajaxrelation(request):
    memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
    relationdata=tbl_relationtype.objects.get(id=request.GET.get('did'))
    passdata=str(relationdata.relation_type)
    print(passdata)
    if passdata=="Daughter-in-law" or passdata=="Son-in-law" or passdata=="Granddaughter" or passdata=="Grandson":
        print("Hai")
        datacount=tbl_relatives.objects.filter(member_name=memberdata).count()
        print(datacount)
        data=tbl_relatives.objects.filter(member_name=memberdata)
        return render(request,"Member/Ajaxrelation.html",{'rdata':data,'content':passdata})
    else:
        return render(request,"Member/Ajaxrelation.html",{'adata':memberdata,'content':passdata})

def viewweeklycollection(request):

    if 'reid' in request.session:
        relativedata=tbl_relatives.objects.get(id=request.session["reid"])
        data=tbl_weeklycollection.objects.all().last()
        cpayment=tbl_weeklycollectionpayment.objects.filter(relative_name=relativedata,
        weeklycollection_id=data).count()
        warray=[i for i  in range(1,49)]
        data=tbl_weeklycollection.objects.all().last()
        return render(request,"Member/viewweeklycollection.html",{'datas':data,'array':warray,
        'weekcount':cpayment,'data':relativedata})
    elif 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        data=tbl_weeklycollection.objects.all().last()
        cpayment=tbl_weeklycollectionpayment.objects.filter(member_name=memberdata,
        weeklycollection_id=data).count()
        warray=[i for i  in range(1,49)]
        data=tbl_weeklycollection.objects.all().last()
        return render(request,"Member/viewweeklycollection.html",{'datas':data,'array':warray,
        'weekcount':cpayment,'data1':memberdata})
    else:
        return redirect("Guest:login")
        
def viewmonthlycollection(request):
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        data=tbl_monthlycollection.objects.all().last()
        cpayment=tbl_monthlycollectionpayment.objects.filter(member_name=memberdata,monthlycollection_id=data).count()
        marray=[i for i  in range(1,13)] 
        return render(request,"Member/viewmonthlycollection.html",{'datas':data,'array':marray,
        'monthcount':cpayment,'data1':memberdata})
    else:
        return redirect("Guest:login")
    

# def designpayment(request):
#     return render(request,"Member/DesignPayment.html")

def paysucessful(request):
    if 'mid' in request.session:
        return render(request,"Member/paysucessful.html")
    elif 'reid' in request.session:
        return render(request,"Member/paysucessful.html")
    else:
       return redirect("Guest:login")
    #return render(request,"Member/paysucessful.html")

def runpayment(request):
    if 'mid' in request.session:
        return render(request,"Member/runpayment.html")
    elif 'reid' in request.session:
        return render(request,"Member/runpayment.html")
    else:
        return redirect("Guest:login")
    #return render(request,"Member/runpayment.html")

def logout(request):
    if 'mid' in request.session and 'reid' in request.session:
        del request.session["mid"]
        del request.session["reid"]
        return redirect("Guest:login")
    elif 'mid' in request.session:
        del request.session["mid"]
        return redirect("Guest:login")
    else:
        del request.session["reid"]
        return redirect("Guest:login")

def weeklycollectionpayment(request,wid):
    if 'reid' in request.session:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        wdata=tbl_weeklycollection.objects.get(id=wid)
        if request.method=="POST":
            tbl_weeklycollectionpayment.objects.create(relative_name=rdata,weeklycollection_id=wdata)
            return redirect("Member:runpayment")
        else:
            return render(request,"Member/DesignPayment.html")
    elif 'mid' in request.session:
        mdata=tbl_memberadding.objects.get(id=request.session["mid"])
    
        wdata=tbl_weeklycollection.objects.get(id=wid)
        if request.method=="POST":
            tbl_weeklycollectionpayment.objects.create(member_name=mdata,weeklycollection_id=wdata)
            return redirect("Member:runpayment")
        else:
            return render(request,"Member/DesignPayment.html")    
    else:
        return redirect("Guest:login")

def monthlycollectionpayment(request,mcid):
    medata=tbl_memberadding.objects.get(id=request.session["mid"])
    
    mdata=tbl_monthlycollection.objects.get(id=mcid)
    if request.method=="POST":
        tbl_monthlycollectionpayment.objects.create(member_name=medata,monthlycollection_id=mdata)
        return redirect("Member:runpayment")
    else:
        return render(request,"Member/DesignPayment.html")

def scholarshipview(request):
    stdata=tbl_scholarshiptype.objects.all()
    sndata=tbl_scholarshipname.objects.all()
    if 'mid' in request.session:
        mdata=tbl_memberadding.objects.get(id=request.session["mid"])
        return render(request,"Member/scholarshipview.html",{'sndata':sndata,'sdata':stdata,'data1':mdata})
    elif 'reid' in request.session:
        mdata=tbl_relatives.objects.get(id=request.session["reid"])
        return render(request,"Member/scholarshipview.html",{'sndata':sndata,'sdata':stdata,'data':mdata})
    else:
        return redirect("Guest:login")
def ajaxscholarship(request):
    sdata=tbl_scholarshiptype.objects.get(id=request.GET.get('sid'))
    sndata=tbl_scholarshipname.objects.filter(scholarship_type=sdata)
    return render(request,"Member/Ajaxscholarship.html",{'sndata':sndata})

def scholarshipapply(request,said):
    sdata=tbl_scholarshipname.objects.get(id=said)
    if 'mid' in request.session:
        data=tbl_memberadding.objects.get(id=request.session["mid"])
        if request.method=="POST":
            tbl_scholarshipapply.objects.create(member_name=data,scholarship_name=sdata,
            document=request.FILES.get('proof'))
            return redirect("Member:homepage")
        else:
           # return render(request,"Member/scholarshipapply.html")
            return render(request,"Member/scholarshipapply.html",{'data':data,'sadata':sdata})
    elif 'reid' in request.session:
        data=tbl_relatives.objects.get(id=request.session["reid"])
        if request.method=="POST":
            tbl_scholarshipapply.objects.create(relative_name=data,scholarship_name=sdata,
            document=request.FILES.get('proof'))
            return redirect("Member:homepage")
        else:
            #return render(request,"Member/scholarshipapply.html")
            return render(request,"Member/scholarshipapply.html",{'data1':data,'sadata':sdata})
    else:
        return redirect("Member:scholarshipapply")

def scholarshipstatus(request):
    if 'mid' in request.session:
        data=tbl_memberadding.objects.get(id=request.session["mid"])
        sdata=tbl_scholarshipapply.objects.filter(member_name=data)
        return render(request,"Member/scholarshipstatus.html",{'datas':sdata,'data1':data})
    elif 'reid' in request.session:
        data=tbl_relatives.objects.get(id=request.session["reid"])
        sdata=tbl_scholarshipapply.objects.filter(relative_name=data)
        return render(request,"Member/scholarshipstatus.html",{'datas':sdata,'data':data})
    else:
        return redirect("Member:homepage")

def deleterelative(request,rdid):
    data=tbl_relatives.objects.get(id=rdid)
    data.inactive=2
    data.save()
    return redirect("Member:relatives")

def viewelection(request,eid):
    cdate=date.today()
    if 'mid' in request.session:
        edata=tbl_electiondeclaration.objects.get(id=eid)
        return render(request,"Member/viewelection.html",{'edata':edata,'mess':1,'cdate':cdate})
    else:
        edata=tbl_electiondeclaration.objects.get(id=eid)
        return render(request,"Member/viewelection.html",{'edata':edata,'cdate':cdate})

def electionapply(request,eaid):
    #if 'mid' in request.session:
       # data=tbl_memberadding.objects.get(id=request.session["mid"])
    if 'mid' in request.session:
        pdata=tbl_electionposition.objects.all()   
        edata=tbl_electiondeclaration.objects.get(id=eaid)
        cdate=date.today()
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        if request.method=="POST":
            if cdate<=edata.nomination_date:
                ptype=tbl_electionposition.objects.get(id=request.POST.get('ptype'))
                tbl_electionapply.objects.create(member_name=memberdata,election_name=edata,
                election_position=ptype)
                return redirect("Member:homepage")
            else:
                return redirect("Member:homepage")
        else:
            return render(request,"Member/electionapply.html",{'edata':edata,'pdata':pdata,'data1':memberdata})
    else:
        return redirect("Guest:login")
def electionapplystatusview(request):
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        data=tbl_electionapply.objects.filter(member_name=memberdata)
        return render(request,"Member/viewelectionapplystatus.html",{'datas':data,'data1':memberdata})
    else:
        return redirect("Guest:login")

def viewcandidate(request,ecid):
    staues=[1,3,4]
    edata=tbl_electiondeclaration.objects.get(id=ecid)
    data=tbl_electionapply.objects.filter(status__in=staues,election_name=edata)
    return render(request,"Member/viewcandidate.html",{'data':data})

def votenow(request,cvid):
    if 'mid' in request.session:
        mdata=tbl_memberadding.objects.get(id=request.session["mid"]) # take member data
        vdata=tbl_electiondeclaration.objects.get(id=cvid) # from passing value take electiondeclaration Data
        voteddatacount=tbl_voting.objects.filter(member_name=mdata).count() # count of Voted by member
        j=0 #initalize j=0 for indexing for arrays defined below
        parray=[0 for i in range(1,voteddatacount+1)] # Decalare array for store election Application id From voted data of logined member
        parrays=[0 for i in range(1,voteddatacount+1)] # Decalare array for store election Postion id From voted data of logined member
        voteddata=tbl_voting.objects.filter(member_name=mdata) # Data of Voted by member
        for i in voteddata: # for loop for store postion and application id from voted data
            parray[j]=i.election_apply.id #store application id to parray
            parrays[j]=i.election_apply.election_position.id #store position to parray
            j=j+1 #increment index of array
        votedata=tbl_electionapply.objects.filter(status=1,election_name=vdata) #select data from election apply form status=1 and election we choosed
        return render(request,"Member/votenow.html",{'data':votedata,'voted':parray,'p':parrays,'mdata':mdata})
    elif 'reid' in request.session:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        voteddatacount=tbl_voting.objects.filter(relative_name=rdata).count()
        j=0
        parray=[0 for i in range(1,voteddatacount+1)]
        parrays=[0 for i in range(1,voteddatacount+1)]
        voteddata=tbl_voting.objects.filter(relative_name=rdata)
        for i in voteddata:
            parray[j]=i.election_apply.id
            parrays[j]=i.election_apply.election_position.id
            j=j+1
        vdata=tbl_electiondeclaration.objects.get(id=cvid)
        votedata=tbl_electionapply.objects.filter(status=1,election_name=vdata)
        return render(request,"Member/votenow.html",{'data':votedata,'voted':parray,'p':parrays,'mdata':rdata})
    else:
        return redirect("Member:homepage")

def vote(request,vid):
    if 'mid' in request.session:
        memdata=tbl_memberadding.objects.get(id=request.session["mid"]) #member data 
        vdata=tbl_electionapply.objects.get(id=vid) #electionapply data
        
        datacount=tbl_voting.objects.filter(member_name=memdata).count() #count of member voted
        if datacount>0:
            datas=tbl_voting.objects.filter(member_name=memdata) #voted data of member
            ps=[0 for i in range(0,datacount)] #array for store postion
            ele=[0 for i in range(0,datacount)] #array for store applyid
            j=0 #index of array
            for i in datas:
                ps[j]=i.election_apply.election_position.id #store postions
                ele[j]=i.election_apply.id #store applicationid
            electid=vdata.election_name.id #election id 
            position=vdata.election_position.id #positionid
            if electid in ele and position in ps:
                return redirect("Member:homepage")
            else:
                tbl_voting.objects.create(election_apply=vdata,member_name=memdata)
                return redirect("Member:homepage")
        else:
            tbl_voting.objects.create(election_apply=vdata,member_name=memdata)
            return redirect("Member:homepage")
    else:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        vdata=tbl_electionapply.objects.get(id=vid)
        
        datacount=tbl_voting.objects.filter(relative_name=rdata).count()
        if datacount>0:
            datas=tbl_voting.objects.filter(relative_name=rdata)
            ps=[0 for i in range(0,datacount)]
            ele=[0 for i in range(0,datacount)]
            j=0
            for i in datas:
                ps[j]=i.election_apply.election_position.id
                ele[j]=i.election_apply.id
            electid=vdata.election_name.id
            position=vdata.election_position.id
            if electid in ele and position in ps:
                return redirect("Member:homepage")
            else:
                tbl_voting.objects.create(election_apply=vdata,relative_name=rdata)
                return redirect("Member:homepage")
        else:
            tbl_voting.objects.create(election_apply=vdata,relative_name=rdata)
            return redirect("Member:homepage")

def viewevents(request):
    data=tbl_events.objects.all()
    if 'mid' in request.session:
        mdata=tbl_memberadding.objects.get(id=request.session["mid"])
        return render(request,"Member/viewevents.html",{'datas':data,'data1':mdata})
    elif 'reid' in request.session:
        mdata=tbl_relatives.objects.get(id=request.session["reid"])
        return render(request,"Member/viewevents.html",{'datas':data,'data':mdata})
    else:
        return redirect("Guest:login")

def complaint(request):
    if 'mid' in request.session:
        mdata=tbl_memberadding.objects.get(id=request.session["mid"])
        data=tbl_complaint.objects.filter(member_name=mdata)
        if request.method=="POST":
            tbl_complaint.objects.create(title=request.POST.get('txt_title'),
            content=request.POST.get('txt_content'),member_name=mdata)
            return render(request,"Member/complaint.html",{'datas':data,'data1':mdata})
        else:
            return render(request,"Member/complaint.html",{'datas':data,'data1':mdata})
    elif 'reid' in request.session:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        data=tbl_complaint.objects.filter(relative_name=rdata)
        if request.method=="POST":
            tbl_complaint.objects.create(title=request.POST.get('txt_title'),
            content=request.POST.get('txt_content'),relative_name=rdata)
            return render(request,"Member/complaint.html",{'datas':data,'data':rdata})
        else:
            return render(request,"Member/complaint.html",{'datas':data,'data':rdata})
    else:
        return redirect("Member:homepage")

def feedback(request):
    if 'mid' in request.session:
        mdata=tbl_memberadding.objects.get(id=request.session["mid"])
        if request.method=="POST":
            tbl_feedback.objects.create(content=request.POST.get('txt_content'),
            member_name=mdata)
            return render(request,"Member/feedback.html",{'data1':mdata})
        else:
            return render(request,"Member/feedback.html",{'data1':mdata})
    elif 'reid' in request.session:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        if request.method=="POST":
            tbl_feedback.objects.create(content=request.POST.get('txt_content'),
            relative_name=rdata)
            return render(request,"Member/feedback.html",{'data':rdata})
        else:
            return render(request,"Member/feedback.html",{'data':rdata})
    else:
        return redirect("Member:homepage")

def chittyfunding(request):
    cdata=tbl_chitty.objects.all()
    pdata=tbl_proof.objects.all()
    
    if 'mid' in request.session:
        data=tbl_memberadding.objects.get(id=request.session["mid"]) 
        if request.method=="POST":
            ptype=tbl_proof.objects.get(id=request.POST.get('ptype'))
            chitty=tbl_chitty.objects.get(id=request.POST.get('chitty'))
            cjoincount=tbl_chittyjoin.objects.filter(chittydata=chitty,memberdata=data).count()
            if cjoincount>0:
                cfcount=tbl_chittyfunding.objects.filter(chitty_name=chitty,member_name=data,status=3).count()
                if cfcount>0:
                    return render(request,"Member/All.html",{'mess1':1})
                else:
                    tbl_chittyfunding.objects.create(member_name=data,
                        document=request.FILES.get('proof'),chitty_name=chitty,proof_name=ptype)
                    return redirect("Member:homepage")
            else:
            # return render(request,"Member/scholarshipapply.html")
                return render(request,"Member/chittyfunding.html",{'chitty':cdata,'proof':pdata,'data1':data,'mess3':1})
        else:
            return render(request,"Member/chittyfunding.html",{'chitty':cdata,'proof':pdata,'data1':data})
    elif 'reid' in request.session:
        data=tbl_relatives.objects.get(id=request.session["reid"])
        if request.method=="POST":
            ptype=tbl_proof.objects.get(id=request.POST.get('ptype'))
            chitty=tbl_chitty.objects.get(id=request.POST.get('chitty'))
            cjoincount=tbl_chittyjoin.objects.filter(chittydata=chitty,relative=data).count()
            if cjoincount>0:
                cfcount=tbl_chittyfunding.objects.filter(chitty_name=chitty,relative_name=data,status=3).count()
                if cfcount>0:
                    return render(request,"Member/All.html",{'mess1':1})
                else:
                    tbl_chittyfunding.objects.create(relative_name=data,document=request.FILES.get('proof'),
                    chitty_name=chitty,proof_name=ptype)
                    return redirect("Member:homepage")
            else:
                return render(request,"Member/chittyfunding.html",{'chitty':cdata,'proof':pdata,'data':data,'mess3':1})
        else:
            return render(request,"Member/chittyfunding.html",{'chitty':cdata,'proof':pdata,'data':data})
            #return render(request,"Member/scholarshipapply.html")
    else:
        return render(request,"Member/chittyfunding.html")

def chittyfundingstatusview(request):
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        mdata=tbl_chittyfunding.objects.filter(member_name=memberdata)
        return render(request,"Member/chittyfundingstatus.html",{'status':mdata,'data1':memberdata})
    elif 'reid' in request.session:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        data=tbl_chittyfunding.objects.filter(relative_name=rdata)
        return render(request,"Member/chittyfundingstatus.html",{'status1':data,'data1':rdata})
    else:
        return redirect("Member:homepage")

def loanreport(request):
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        if request.method=="POST":
            if request.POST.get('fdate')!="" and request.POST.get('edate'):
                datas=tbl_loanapply.objects.filter(member_name=memberdata,status=3,
                apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
                return render(request,"Member/loanreport.html",{'data':datas})
            elif request.POST.get('fdate')!="":
                datas=tbl_loanapply.objects.filter(member_name=memberdata,status=3,
                apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
                return render(request,"Member/loanreport.html",{'data':datas})
            else:
                datas=tbl_loanapply.objects.filter(member_name=memberdata,status=3,
                apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
                return render(request,"Member/loanreport.html",{'data':datas})
        else:
            return render(request,"Member/loanreport.html")
    else:
        return render(request,"Member/loanreport.html")

def chittyreport(request):
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        if request.method=="POST":
            if request.POST.get('fdate')!="" and request.POST.get('edate'):
                datas=tbl_chittyjoin.objects.filter(memberdata=memberdata,status=3,
                apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
                return render(request,"Member/chittyreport.html",{'data':datas})
            elif request.POST.get('fdate')!="":
                datas=tbl_chittyjoin.objects.filter(memberdata=memberdata,status=3,
                apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
                return render(request,"Member/chittyreport.html",{'data':datas})
            else:
                datas=tbl_chittyjoin.objects.filter(memberdata=memberdata,status=3,
                apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
                return render(request,"Member/chittyreport.html",{'data':datas})
        else:
            return render(request,"Member/chittyreport.html")
    elif 'reid' in request.session:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        if request.method=="POST":
            if request.POST.get('fdate')!="" and request.POST.get('edate'):
                datas=tbl_chittyjoin.objects.filter(relative=rdata,status=3,
                apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
                return render(request,"Member/chittyreport.html",{'data1':datas})
            elif request.POST.get('fdate')!="":
                datas=tbl_chittyjoin.objects.filter(relative=rdata,status=3,
                apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
                return render(request,"Member/chittyreport.html",{'data1':datas})
            else:
                datas=tbl_chittyjoin.objects.filter(relative=rdata,status=3,
                apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
                return render(request,"Member/chittyreport.html",{'data1':datas})
        else:
            return render(request,"Member/chittyreport.html")
    else:
        return render(request,"Member/chittyreport.html")
   

def scholarshipreport(request):
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        if request.method=="POST":
            if request.POST.get('fdate')!="" and request.POST.get('edate'):
                datas=tbl_scholarshipapply.objects.filter(member_name=memberdata,status=3,
                apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
                return render(request,"Member/scholarshipreport.html",{'data':datas})
            elif request.POST.get('fdate')!="":
                datas=tbl_scholarshipapply.objects.filter(member_name=memberdata,status=3,
                apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
                return render(request,"Member/scholarshipreport.html",{'data':datas})
            else:
                datas=tbl_scholarshipapply.objects.filter(member_name=memberdata,status=3,
                apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
                return render(request,"Member/scholarshipreport.html",{'data':datas})
        else:
            return render(request,"Member/scholarshipreport.html")
    elif 'reid' in request.session:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        if request.method=="POST":
            if request.POST.get('fdate')!="" and request.POST.get('edate'):
                datas=tbl_scholarshipapply.objects.filter(relative_name=rdata,status=3,
                apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
                return render(request,"Member/scholarshipreport.html",{'data1':datas})
            elif request.POST.get('fdate')!="":
                datas=tbl_scholarshipapply.objects.filter(relative_name=rdata,status=3,
                apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
                return render(request,"Member/scholarshipreport.html",{'data1':datas})
            else:
                datas=tbl_scholarshipapply.objects.filter(relative_name=rdata,status=3,
                apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
                return render(request,"Member/scholarshipreport.html",{'data1':datas})
        else:
            return render(request,"Member/scholarshipreport.html")
    else:
        return render(request,"Member/scholarshipreport.html")