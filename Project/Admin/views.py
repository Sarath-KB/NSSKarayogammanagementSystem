from django.shortcuts import render,redirect
from Admin.models import *
from Member.models import *
from Finance.models import *
from datetime import date
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def district(request):
    districtdata=tbl_district.objects.all()

    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get('txt_district'))
        return render(request,"Admin/District.html",{'data':districtdata})
    else:
        return render(request,"Admin/District.html",{'data':districtdata})
        
def category(request):
    categorydata=tbl_category.objects.all()
    if request.method=="POST":
        tbl_category.objects.create(category_name=request.POST.get('category'))
        return render(request,"Admin/category.html",{'data':categorydata})
    else:
           return render(request,"Admin/category.html",{'data':categorydata})
          
def deldis(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Admin:district")

def delcat(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect("Admin:category")

def disedit(request,did):
    editdata=tbl_district.objects.get(id=did)
    if request.method=="POST":
        editdata.district_name=request.POST.get('txt_district')
        editdata.save()
        return redirect("Admin:district")
    else:
         return render(request,"Admin/District.html",{'edit':editdata})

def catedit(request,cid):
    editdata=tbl_category.objects.get(id=cid)
    if request.method=="POST":
        editdata.category_name=request.POST.get('category')
        editdata.save()
        return redirect("Admin:category")
    else:
         return render(request,"Admin/category.html",{'edit':editdata})

def place(request):
    districtdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=="POST":
        dis=tbl_district.objects.get(id=request.POST.get('district'))
        tbl_place.objects.create(place_name=request.POST.get('txt_place'),district=dis)
        return render(request,"Admin/place.html",{'district':districtdata,'place':placedata})
    else:
        return render(request,"Admin/place.html",{'district':districtdata,'place':placedata})

def deleteplace(request,pid):
    tbl_place.objects.get(id=pid).delete()
    return redirect("Admin:place")

def subcategory(request):
    categorydata=tbl_category.objects.all()
    subcategorydata=tbl_subcategory.objects.all()
    if request.method=="POST":
        cat=tbl_category.objects.get(id=request.POST.get('category'))
        tbl_subcategory.objects.create(subcategory_name=request.POST.get('txt_subcat'),category=cat)
        return render(request,"Admin/subcategory.html",{'category':categorydata,'subcat':subcategorydata})
    else:
        return render(request,"Admin/subcategory.html",{'category':categorydata,'subcat':subcategorydata})
    
def deletesubcat(request,scatid):
    tbl_subcategory.objects.get(id=scatid).delete()
    return redirect("Admin:subcategory")

def ajaxlocation(request):
    districtdata=tbl_district.objects.get(id=request.GET.get('disd'))
    placedata=tbl_place.objects.filter(district=districtdata)
    return render(request,"Admin/Ajaxlocation.html",{'place':placedata})

def memberadding(request):
    districtdata=tbl_district.objects.all()
    memberdata=tbl_memberadding.objects.all()
    if request.method=="POST":
        loca=tbl_place.objects.get(id=request.POST.get('place'))
        tbl_memberadding.objects.create(member_name=request.POST.get('txt_name'),
        age=request.POST.get('txt_age'),
        contact=request.POST.get('txt_contact'),
        email=request.POST.get('txt_email'),
        address=request.POST.get('txt_address'),
        photo=request.FILES.get('photo'),
        #password=request.POST.get('pass'),
        gender=request.POST.get('gender'),place=loca)
        return redirect("Admin:memberadding")
    else:
        return render(request,"Admin/memberadding.html",{'district':districtdata,'member':memberdata})

def financehead(request):
    financedata=tbl_financehead.objects.all()
    if request.method=="POST":
        tbl_financehead.objects.create(head_name=request.POST.get('txt_name'),
        user_name=request.POST.get('txt_username'),
        password=request.POST.get('pass'),
        fdate=request.POST.get('fdate'),
        tdate=request.POST.get('tdate'))
        return redirect("Admin:financehead.html")
    else:
        return render(request,"Admin/financehead.html",{'finance':financedata})

def scheme(request):
    schemedata=tbl_scheme.objects.all()
    if request.method=="POST":
        tbl_scheme.objects.create(scheme_name=request.POST.get('txt_scheme'))
        return redirect("Admin:scheme")
    else:
        return render(request,"Admin/scheme.html",{'scheme':schemedata})

def deletefinancehead(request,fhid):
    tbl_financehead.objects.get(id=fhid).delete()
    return redirect("Admin:financehead")

def editfinancehead(request,fhid):
    editdata=tbl_financehead.objects.get(id=fhid)
    if request.method=="POST":
        editdata.head_name=request.POST.get('txt_name')
        editdata.save()
        return redirect("Admin:financehead")
    else:
         return render(request,"Admin/financehead.html",{'edit':editdata})

def deletescheme(request,sid):
    tbl_scheme.objects.get(id=sid).delete()
    return redirect("Admin:scheme")

def editscheme(request,sid):
    editdata=tbl_scheme.objects.get(id=sid)
    if request.method=="POST":
        editdata.scheme_name=request.POST.get('txt_scheme')
        editdata.save()
        return redirect("Admin:scheme")
    else:
         return render(request,"Admin/scheme.html",{'edit':editdata})

def deletemember(request,mid):
    mess=""
    tot=0
    t=0
    data=tbl_memberadding.objects.get(id=mid)
    name=data.member_name
    email=data.email
    loancount=tbl_loanapply.objects.filter(member_name=data).count()
    chcount=tbl_chittyjoin.objects.filter(memberdata=data).count()
    if loancount>0:
        dataloan=tbl_loanapply.objects.filter(member_name=data)
        for i in dataloan:
            ld=tbl_addloanname.objects.get(id=i.loan_name.id)

            ldcal=tbl_loancalender.objects.get(loan_name=ld)
            lp=tbl_loanapply.objects.get(id=i.id)
            ncount=int(ldcal.no_installment)
            repaycount=tbl_repaymentloan.objects.filter(loanapply=lp,member=data).count()
            cl=ncount-repaycount
            if cl==0:
                continue
            else:
                tot=tot+cl
    elif chcount>0:
        ch=tbl_chittyjoin.objects.filter(memberdata=data)
        for i in ch:
            chitdata=tbl_chitty.objects.get(id=i.chittydata.id)
            ccalender=tbl_chittycalender.objects.get(chittydata=chitdata)
            cjdata=tbl_chittyjoin.objects.get(id=i.id)
            cncount=int(ccalender.no_installment)
            rcount=tbl_paymentchitty.objects.filter(chitty_apply=cjdata).count()
            cc=cncount-rcount
            if cc==0:
                continue
            else:
                t=t+cc
    else:
        tot=0
        t=0
    if tot >0 and t>0:
        mess="Your Loan Repayment is Pending Count"+str(tot)+"."+" "+"Your Chitty Pening is "+str(t)
        send_mail(
            'Respected Sir/Madam'+name,#subject
            "\r"+str(mess),#body
            settings.EMAIL_HOST_USER,
            [email],
        )
        return redirect("Admin:memberadding")
    elif tot>0:
        mess="Your Loan Repayment is Pending Count"+str(tot)+"."
        send_mail(
            'Respected Sir/Madam'+name,#subject
            "\r"+str(mess),#body
            settings.EMAIL_HOST_USER,
            [email],
        )
        return redirect("Admin:memberadding") 
    elif t>0:
        mess="Your Loan Repayment is Pending Count"+str(tot)+"."+" "+"Your Chitty Pening is "+str(t)
        send_mail(
            'Respected Sir/Madam'+name,#subject
            "\r"+str(mess),#body
            settings.EMAIL_HOST_USER,
            [email],
           
        )
        return redirect("Admin:memberadding") 
    else:
        mess="You Are Eligible for Moving From Karayogam"
        send_mail(
            'Respected Sir/Madam'+name,#subject
            "\r"+str(otmessp),#body
            settings.EMAIL_HOST_USER,
            [email],
        )
        data.inactive=2
        data.save()
        return redirect("Admin:memberadding") 

def passedmember(request,mid):       
    mdata=tbl_memberadding.objects.get(id=mid)
    agearray=[]
    relativedata=tbl_relatives.objects.filter(member_name=mdata)

    for i in relativedata:
        agearray.append(i.age)

    hightestage=max(agearray)

    relativeremovedata=tbl_relatives.objects.get(age=hightestage,member_name=mdata)
    
    mdata.member_name,relativeremovedata.relative_name=relativeremovedata.relative_name,mdata.member_name
    mdata.age,relativeremovedata.age=relativeremovedata.age,mdata.age
    mdata.photo,relativeremovedata.photo=relativeremovedata.photo,mdata.photo
    mdata.email,relativeremovedata.email=relativeremovedata.email,mdata.email
    mdata.contact,relativeremovedata.contact=relativeremovedata.contact,mdata.contact
    mdata.address,relativeremovedata.address=relativeremovedata.address,mdata.address
    mdata.password,relativeremovedata.password=relativeremovedata.password,mdata.password
    mdata.gender,relativeremovedata.gender=relativeremovedata.gender,mdata.gender
    # membername=mdata.member_name
    # memberage=mdata.age
    # memberemail=mdata.email
    # membercontact=mdata.contact
    # memberphoto=mdata.photo
    # memberpassword=mdata.password
    # memberaddress=mdata.address
    # membergender=mdata.gender

    # relativeremovedata.relative_name=membername
    # relativeremovedata.age=memberage
    # relativeremovedata.email=memberemail
    # relativeremovedata.photo=memberphoto
    # relativeremovedata.contact=membercontact
    # relativeremovedata.address=memberaddress
    # relativeremovedata.gender=membergender
    
    # relativename=relativeremovedata.relative_name
    # relativeage=relativeremovedata.age
    # relativeaddress=relativeremovedata.address
    # relativecontact=relativeremovedata.contact
    # relativeemail=relativeremovedata.email
    # relativephoto=relativeremovedata.photo
    # relativepassword=relativeremovedata.password
    # relativegender=relativeremovedata.gender

    # mdata.member_name=relativename
    # mdata.age=relativeage
    # mdata.address=relativeaddress
    # mdata.contact=relativecontact
    # mdata.email=relativeemail
    # mdata.photo=relativephoto
    # mdata.password=relativepassword
    # mdata.gender=relativegender

    # data.inactive=3
    relativeremovedata.inactive=3
    mdata.save()
    
    relativeremovedata.save()
     
    return redirect("Admin:memberadding") 

def loan(request):
    loandata=tbl_loan.objects.all()
    if request.method=="POST":
        tbl_loan.objects.create(loan_name=request.POST.get('txt_loan'))
        return redirect("Admin:loan")
    else:
         return render(request,"Admin/loan.html",{'loan':loandata})
        
def deleteloan(request,lid):
    tbl_loan.objects.get(id=lid).delete()
    return redirect("Admin:loan")   

def editloan(request,lid):
    editloandata=tbl_loan.objects.get(id=lid)
    if request.method=="POST":
        editloandata.loan_name=request.POST.get('txt_loan')
        editloandata.save()
        return redirect("Admin:loan")
    else:
         return render(request,"Admin/loan.html",{'editloan':editloandata})

def homepage(request):
    membercount=tbl_memberadding.objects.filter(inactive__lt=2).count()
    memberdata=tbl_memberadding.objects.all()
    relativecount=tbl_relatives.objects.filter(inactive__lt=2).count()
    reldata=tbl_relatives.objects.all()
    lcount=tbl_addloanname.objects.all().count()
    scount=tbl_scholarshipname.objects.all().count()
   
    return render(request,"Admin/homepage.html",{'mcount':membercount,'mdata':memberdata,'rcount':relativecount,'rdata':reldata,'lcount':lcount,'scount':scount})

def proof(request):
    proofdata=tbl_proof.objects.all()
    if request.method=="POST":
        tbl_proof.objects.create(proof_name=request.POST.get('txt_proof'))
        return redirect("Admin:proof")
    else:
         return render(request,"Admin/proof.html",{'proof':proofdata})

def deleteproof(request,pid):
    tbl_proof.objects.get(id=pid).delete()
    return redirect("Admin:proof")

def editproof(request,pid):
    editdata=tbl_proof.objects.get(id=pid)
    if request.method=="POST":
        editdata.proof_name=request.POST.get('txt_proof')
        editdata.save()
        return redirect("Admin:proof")
    else:
         return render(request,"Admin/proof.html",{'edit':editdata})
    
def relationtype(request):
    relationtypedata=tbl_relationtype.objects.all()
    if request.method=="POST":
        tbl_relationtype.objects.create(relation_type=request.POST.get('txt_relationtype'))
        return redirect("Admin:relationtype")
    else:
        return render(request,"Admin/relationtype.html",{'relationtype':relationtypedata})

def deleterelationtype(request,rid):
    tbl_relationtype.objects.get(id=rid).delete()
    return redirect("Admin:relationtype")

def editrelationtype(request,rid):
    editdata=tbl_relationtype.objects.get(id=rid)
    if request.method=="POST":
        editdata.relation_type=request.POST.get('txt_relationtype')
        editdata.save()
        return redirect("Admin:relationtype")
    else:
        return render(request,"Admin/relationtype.html",{'edit':editdata})

def scholarshiptype(request):
    sdata=tbl_scholarshiptype.objects.all()
    if request.method=="POST":
        tbl_scholarshiptype.objects.create(scholarship_type=request.POST.get('txt_scholarship'))
        return redirect("Admin:scholarshiptype")
    else:
        return render(request,"Admin/scholarshiptype.html",{'data':sdata})

def deletescholarshiptype(request,sid):
    tbl_scholarshiptype.objects.get(id=sid).delete()
    return redirect("Admin:scholarshiptype")

def scholarshipname(request):
    sdata=tbl_scholarshiptype.objects.all()
    data=tbl_proof.objects.all()
    sndata=tbl_scholarshipname.objects.all()
    if request.method=="POST":
        scdata=tbl_scholarshiptype.objects.get(id=request.POST.get('stype'))
        ptdata=tbl_proof.objects.get(id=request.POST.get('ptype'))
        tbl_scholarshipname.objects.create(scholarship_name=request.POST.get('txt_sname'),
        scholarship_details=request.POST.get('txt_details'),scholarship_type=scdata,proof_name=ptdata)
        return render(request,"Admin/scholarshipname.html",{'data':sdata,'pdata':data,'sndata':sndata})
    else:
       
        return render(request,"Admin/scholarshipname.html",{'data':sdata,'pdata':data,'sndata':sndata})

def deletescholarshipname(request,snid):
    tbl_scholarshipname.objects.get(id=snid).delete()
    return redirect("Admin:scholarshipname")

def scholarshipapplications(request):
    mdata=tbl_memberadding.objects.all()
    rdata=tbl_relatives.objects.all()
    mappdata=tbl_scholarshipapply.objects.filter(member_name__in=mdata,status=0)
    rappdata=tbl_scholarshipapply.objects.filter(relative_name__in=rdata,status=0)
    return render(request,"Admin/viewscholarshipapply.html",{'data':mappdata,'data1':rappdata})

def scholarshipaccept(request,said):
    acceptdata=tbl_scholarshipapply.objects.get(id=said)
    acceptdata.status=1
    acceptdata.save()
    return redirect("Admin:scholarshipapplications")

def scholarshipreject(request,srid):
    rejectdata=tbl_scholarshipapply.objects.get(id=srid)
    rejectdata.status=2
    rejectdata.save()
    return redirect("Admin:scholarshipapplications")

def scholarshipacceptlist(request):
    mdata=tbl_memberadding.objects.all()
    rdata=tbl_relatives.objects.all()
    mappdata=tbl_scholarshipapply.objects.filter(member_name__in=mdata,status=1)|tbl_scholarshipapply.objects.filter(member_name__in=mdata,status=3)
    rappdata=tbl_scholarshipapply.objects.filter(relative_name__in=rdata,status=1)|tbl_scholarshipapply.objects.filter(relative_name__in=rdata,status=3)
   
    return render(request,"Admin/scholarshipacceptlist.html",{'acceptlist':mappdata,
    'acceptlist1':rappdata})



def scholarshiprejectlist(request):
    mdata=tbl_memberadding.objects.all()
    rdata=tbl_relatives.objects.all()
    data=tbl_scholarshipapply.objects.filter(member_name__in=mdata,status=2)
    data1=tbl_scholarshipapply.objects.filter(relative_name__in=rdata,status=2)
    return render(request,"Admin/scholarshiprejectlist.html",{'rejectlist':data,'rejectlist1':data1})

def mlist(request):
    mdata=tbl_memberadding.objects.all()
    rdata=tbl_relatives.objects.all()
    return render(request,"Admin/viewmemberlist.html",{'mdata':mdata,'rdata':rdata})

def rlist(request,mid):
    data=tbl_memberadding.objects.get(id=mid)
    rdata=tbl_relatives.objects.filter(member_name=data)
    return render(request,"Admin/viewrelativelist.html",{'rdata':rdata})

# def memberdelete(request,mdid):
#     tbl_memberadding.objects.get(id=mdid).delete()
#     return redirect("Admin:mlist")

def electionposition(request):
    data=tbl_electionposition.objects.all()
    if request.method=="POST":
        tbl_electionposition.objects.create(election_position=request.POST.get('txt_election'))
        return redirect("Admin:electionposition")
    else:
        return render(request,"Admin/electionposition.html",{'data':data})

def deleteelectionposition(request,eid):
    tbl_electionposition.objects.get(id=eid).delete()
    return redirect("Admin:electionposition")

def electiondeclaration(request):
    data=tbl_electiondeclaration.objects.all()
    if request.method=="POST":
        tbl_electiondeclaration.objects.create(title=request.POST.get('txt_title'),
        details=request.POST.get('txt_details'),nomination_date=request.POST.get('txt_nd'),
        verified_date=request.POST.get('txt_vd'),election_date=request.POST.get('txt_ed'),
        result_date=request.POST.get('txt_rd'))
        return redirect("Admin:electiondeclaration")
    else:
        return render(request,"Admin/electiondeclaration.html",{'data':data})
    #return render(request,"Admin/electiondeclaration.html")

def electiondeclarationdelete(request,edid):
    tbl_electiondeclaration.objects.get(id=edid).delete()
    return redirect("Admin:electiondeclaration")

def electionapplication(request):
    mdata=tbl_memberadding.objects.all()
    
    data=tbl_electionapply.objects.filter(member_name__in=mdata,status=0)
    
    return render(request,"Admin/viewelectionapply.html",{'data':data})

def electionapplyaccept(request,eaid):
    acceptdata=tbl_electionapply.objects.get(id=eaid)
    acceptdata.status=1
    acceptdata.save()
    return redirect("Admin:electionapplication")   

def electionapplyreject(request,erid):
    acceptdata=tbl_electionapply.objects.get(id=erid)
    acceptdata.status=2
    acceptdata.save()
    return redirect("Admin:electionapplication")

def electionapplyacceptlist(request):
    acceptlistdata=tbl_electionapply.objects.filter(status=1) |tbl_electionapply.objects.filter(status__gt=2)
    return render(request,"Admin/viewelectionacceptlist.html",{'data':acceptlistdata})

def viewvote(request):
    #mdata=tbl_memberadding.objects.all()
    #rdata=tbl_relatives.objects.all()
    
    edatacount=tbl_electionapply.objects.all().count()
    positions=[0 for i in range(0,edatacount)]
    countarray=[0 for i in range(0,edatacount)]
    edata=tbl_electionapply.objects.all()
    j=0
    for i in edata:
        counts=tbl_voting.objects.filter(election_apply=i.id).count()
        print(counts)
        countarray[j]=counts
        positions[j]=i.election_position.id
        j=j+1
        
    print(countarray)
    datas=zip(edata,countarray) 
    # vdata=tbl_voting.objects.all()
    # mappdata=tbl_voting.objects.filter(member_name__in=mdata)
    # rappdata=tbl_voting.objects.filter(relative_name__in=rdata)
    return render(request,"Admin/viewvote.html",{'data':datas})

def presidentvotings(request):
    mess="Election Is Declared"

    mess1="Election on Process After Voting  Please Login Again"
    cdate=date.today()
    c=tbl_electiondeclaration.objects.filter(status=0).count()
    dc=tbl_electiondeclaration.objects.filter(election_date=cdate).count()
    rc=tbl_electiondeclaration.objects.filter(result_date=cdate).count()
    if rc>0:
        rcdata=tbl_electiondeclaration.objects.get(status=0,result_date=cdate)
        
        rclast=tbl_electiondeclaration.objects.filter(status=0,result_date=cdate).last()
        statusdata=[1,3,4]
        edatacount=tbl_electionapply.objects.filter(election_position__election_position="President",status__in=statusdata).count()
        countarray=[0 for i in range(0,edatacount)] 
        darray=[0 for i in range(0,edatacount)]
        edata=tbl_electionapply.objects.filter(election_position__election_position="President",status__in=statusdata)
        j=0
        for i in edata:
            counts=tbl_voting.objects.filter(election_apply=i.id).count()
            #print(counts)
            countarray[j]=counts
            darray[j]=counts
            j=j+1
        darray.sort()
        print(len(countarray))
        countmax=darray[j-1]
        for i in edata:
            counts=tbl_voting.objects.filter(election_apply=i.id).count()
            if countmax==counts:
                datakey=tbl_electionapply.objects.get(id=i.id)
                datakey.status=3
                datakey.save()
            else:
                datakey=tbl_electionapply.objects.get(id=i.id)
                datakey.status=4
                datakey.save()
        return redirect("Admin:prelist")
    elif dc>0:
         return  render(request,"Admin/presidentvotings.html",{'mess1':mess1})
    elif c>0:
        return  render(request,"Admin/presidentvotings.html",{'mess':mess})
    else:
        return  render(request,"Admin/presidentvotings.html")
    # mess="Election Is Declared"

    # mess1="Election on Process After Voting  Please Login Again"
    # cdate=date.today()
    # c=tbl_electiondeclaration.objects.filter(status=0).count()
    # dc=tbl_electiondeclaration.objects.filter(election_date=cdate).count()
    # if dc>0:
    #      return  render(request,"Admin/presidentvotings.html",{'mess1':mess1})
    # elif c>0:
    #     return  render(request,"Admin/presidentvotings.html",{'mess':mess})
    # else:
    #     return  render(request,"Admin/presidentvotings.html")
    
    # rc=tbl_electiondeclaration.objects.filter(election_date__gt=cdate,result_date__lte=cdate).count()
    # #print(rc)
    # if rc>0:
    #     statusdata=[1,3,4]
    #     edatacount=tbl_electionapply.objects.filter(election_position__election_position="President",status__in=statusdata).count()
        
    #     countarray=[0 for i in range(0,edatacount)] 
    #     darray=[0 for i in range(0,edatacount)]
    #     edata=tbl_electionapply.objects.filter(election_position__election_position="President",status__in=statusdata)
    #     j=0
    #     for i in edata:
    #         counts=tbl_voting.objects.filter(election_apply=i.id).count()
    #         #print(counts)
    #         countarray[j]=counts
    #         darray[j]=counts
    #         j=j+1
    #     darray.sort()
    #     print(len(countarray))
    #     countmax=darray[j-1]
    #     for i in edata:
    #         counts=tbl_voting.objects.filter(election_apply=i.id).count()
    #         if countmax==counts:
    #             datakey=tbl_electionapply.objects.get(id=i.id)
    #             datakey.status=3
    #             datakey.save()
    #         else:
    #             datakey=tbl_electionapply.objects.get(id=i.id)
    #             datakey.status=4
    #             datakey.save()
        
    #     #print(countarray)
    #     datas=zip(edata,countarray) 
    #     #print(edatacount)
        
    #     return render(request,"Admin/presidentvotings.html",{'data':datas})
    # elif dc>0:
    #     return render(request,"Admin/presidentvotings.html",{'mess1':mess1})
    
    
    # else:
    #     return render(request,"Admin/presidentvotings.html",{'mess':mess})

def secretaryvotings(request):
    mess="Election Is Declared"

    mess1="Election on Process After Voting  Please Login Again"
    cdate=date.today()
    c=tbl_electiondeclaration.objects.filter(status=0).count()
    dc=tbl_electiondeclaration.objects.filter(election_date=cdate).count()
    rc=tbl_electiondeclaration.objects.filter(result_date=cdate).count()
    if rc>0:
        rcdata=tbl_electiondeclaration.objects.get(status=0,result_date=cdate)
        
        rclast=tbl_electiondeclaration.objects.filter(status=0,result_date=cdate).last()
        statusdata=[1,3,4]
        edatacount=tbl_electionapply.objects.filter(election_position__election_position="Secretary",status__in=statusdata).count()
        countarray=[0 for i in range(0,edatacount)] 
        darray=[0 for i in range(0,edatacount)]
        edata=tbl_electionapply.objects.filter(election_position__election_position="Secretary",status__in=statusdata)
        j=0
        for i in edata:
            counts=tbl_voting.objects.filter(election_apply=i.id).count()
            #print(counts)
            countarray[j]=counts
            darray[j]=counts
            j=j+1
        darray.sort()
        print(len(countarray))
        countmax=darray[j-1]
        for i in edata:
            counts=tbl_voting.objects.filter(election_apply=i.id).count()
            if countmax==counts:
                datakey=tbl_electionapply.objects.get(id=i.id)
                datakey.status=3
                datakey.save()
            else:
                datakey=tbl_electionapply.objects.get(id=i.id)
                datakey.status=4
                datakey.save()
        return redirect("Admin:secretarylist")
        
    elif dc>0:
         return  render(request,"Admin/secretaryvotings.html",{'mess1':mess1})
    elif c>0:
        return  render(request,"Admin/secretaryvotings.html",{'mess':mess})
    else:
        return  render(request,"Admin/secretaryvotings.html")
    # mess="Coming Soon........"
    # mess1="Election on Process After Voting  Please Login Again"
    # cdate=date.today()
    # c=tbl_electiondeclaration.objects.filter(nomination_date__lt=cdate,verified_date__lt=cdate).count()
    # dc=tbl_electiondeclaration.objects.filter(election_date=cdate).count()
    # rc=tbl_electiondeclaration.objects.filter(election_date__gte=cdate,result_date__lte=cdate).count()
    # if rc>0:
    #     statusdata=[1,3,4]
        
    #     edatacount=tbl_electionapply.objects.filter(election_position__election_position="Secretary",status__in=statusdata).count()
        
    #     countarray=[0 for i in range(0,edatacount)] 
    #     darray=[0 for i in range(0,edatacount)]
    #     edata=tbl_electionapply.objects.filter(election_position__election_position="Secretary",status__in=statusdata)
    #     j=0
    #     for i in edata:
    #         counts=tbl_voting.objects.filter(election_apply=i.id).count()
    #         #print(counts)
    #         countarray[j]=counts
    #         darray[j]=counts
    #         j=j+1
    #     darray.sort()
    #     print(len(countarray))
    #     countmax=darray[j-1]
    #     for i in edata:
    #         counts=tbl_voting.objects.filter(election_apply=i.id).count()
    #         if countmax==counts:
    #             datakey=tbl_electionapply.objects.get(id=i.id)
    #             datakey.status=3
    #             datakey.save()
    #         else:
    #             datakey=tbl_electionapply.objects.get(id=i.id)
    #             datakey.status=4
    #             datakey.save()
        
    #     #print(countarray)
    #     datas=zip(edata,countarray) 
    #     #print(edatacount)
    #     return render(request,"Admin/secretaryvotings.html",{'data':datas})
    # elif dc>0:
    #     return render(request,"Admin/secretaryvotings.html",{'mess1':mess1})
    # elif c>0:
    #     return render(request,"Admin/secretaryvotings.html",{'mess':mess})
    # else:
    #     return render(request,"Admin/secretaryvotings.html")

def treasurervotings(request):
    mess="Election Is Declared"

    mess1="Election on Process After Voting  Please Login Again"
    cdate=date.today()
    c=tbl_electiondeclaration.objects.filter(status=0).count()
    dc=tbl_electiondeclaration.objects.filter(election_date=cdate).count()
    rc=tbl_electiondeclaration.objects.filter(result_date=cdate).count()
    if rc>0:
        rcdata=tbl_electiondeclaration.objects.get(status=0,result_date=cdate)
        
        rclast=tbl_electiondeclaration.objects.filter(status=0,result_date=cdate).last()
        statusdata=[1,3,4]
        edatacount=tbl_electionapply.objects.filter(election_position__election_position="Treasurer",status__in=statusdata).count()
        countarray=[0 for i in range(0,edatacount)] 
        darray=[0 for i in range(0,edatacount)]
        edata=tbl_electionapply.objects.filter(election_position__election_position="Treasurer",status__in=statusdata)
        j=0
        for i in edata:
            counts=tbl_voting.objects.filter(election_apply=i.id).count()
            #print(counts)
            countarray[j]=counts
            darray[j]=counts
            j=j+1
        darray.sort()
        print(len(countarray))
        countmax=darray[j-1]
        for i in edata:
            counts=tbl_voting.objects.filter(election_apply=i.id).count()
            if countmax==counts:
                datakey=tbl_electionapply.objects.get(id=i.id)
                datakey.status=3
                datakey.save()
            else:
                datakey=tbl_electionapply.objects.get(id=i.id)
                datakey.status=4
                datakey.save()
        return redirect("Admin:treasurerlist")
    elif dc>0:
         return  render(request,"Admin/treasurervotings.html",{'mess1':mess1})
    elif c>0:
        return  render(request,"Admin/treasurervotings.html",{'mess':mess})
    else:
        return  render(request,"Admin/treasurervotings.html")
    # mess="Election Is Declared"

    # mess1="Election on Process After Voting  Please Login Again"
    # cdate=date.today()
    # c=tbl_electiondeclaration.objects.filter(status=0).count()
    # dc=tbl_electiondeclaration.objects.filter(election_date=cdate).count()
    # rc=tbl_electiondeclaration.objects.filter(election_date=cdate).count()
    # if dc>0:
    #      return  render(request,"Admin/treasurervotings.html",{'mess1':mess1})
    # elif c>0:
    #     return  render(request,"Admin/treasurervotings.html",{'mess':mess})
    # else:
    #     return  render(request,"Admin/treasurervotings.html")
    # mess="Coming Soon........"
    # mess1="Election on Process After Voting  Please Login Again"
    # cdate=date.today()
    # c=tbl_electiondeclaration.objects.filter(nomination_date__lt=cdate,verified_date__lt=cdate).count()
    # dc=tbl_electiondeclaration.objects.filter(election_date=cdate).count()
    # rc=tbl_electiondeclaration.objects.filter(election_date__gte=cdate,result_date__lte=cdate).count()
    # if rc>0:
    #     statusdata=[1,3,4]
        
    #     edatacount=tbl_electionapply.objects.filter(election_position__election_position="Treasurer",status__in=statusdata).count()
        
    #     countarray=[0 for i in range(0,edatacount)] 
    #     darray=[0 for i in range(0,edatacount)]
    #     edata=tbl_electionapply.objects.filter(election_position__election_position="Treasurer",status__in=statusdata)
    #     j=0
    #     for i in edata:
    #         counts=tbl_voting.objects.filter(election_apply=i.id).count()
    #         #print(counts)
    #         countarray[j]=counts
    #         darray[j]=counts
    #         j=j+1
    #     darray.sort()
    #     print(len(countarray))
    #     countmax=darray[j-1]
    #     for i in edata:
    #         counts=tbl_voting.objects.filter(election_apply=i.id).count()
    #         if countmax==counts:
    #             datakey=tbl_electionapply.objects.get(id=i.id)
    #             datakey.status=3
    #             datakey.save()
    #         else:
    #             datakey=tbl_electionapply.objects.get(id=i.id)
    #             datakey.status=4
    #             datakey.save()
        
    #     #print(countarray)
    #     datas=zip(edata,countarray) 
    #     #print(edatacount)
    #     return render(request,"Admin/treasurervotings.html",{'data':datas})
    # elif dc>0:
    #     return render(request,"Admin/treasurervotings.html",{'mess1':mess1})
    # elif c>0:
    #     return render(request,"Admin/treasurervotings.html",{'mess':mess})
    # else:
    #     return render(request,"Admin/treasurervotings.html")

def events(request):
    data=tbl_events.objects.all()
    if request.method=="POST":
        tbl_events.objects.create(name=request.POST.get('txt_name'),details=request.POST.get('txt_details'),event_date=request.POST.get('txt_date'))
        return render(request,"Admin/events.html",{'data':data})
    else:
        return render(request,"Admin/events.html",{'data':data})

def deleteevents(request,enid):
    tbl_events.objects.get(id=enid).delete()
    return redirect("Admin:events") 
   

def logout(request):
    if 'aid' in request.session:
        del request.session["aid"]
        return redirect("Guest:login")
    else:
        #del request.session["reid"]
        return redirect("Guest:login")

def presidentlist(request):
    cdate=date.today()
    electiondata=tbl_electiondeclaration.objects.get(status=0,result_date=cdate)
   
    eata=tbl_electiondeclaration.objects.filter(status=0,result_date=cdate).last()
    edatacount=tbl_electionapply.objects.filter(election_position__election_position="President",status__gt=2,election_name=eata).count()
        
    countarray=[0 for i in range(0,edatacount)] 
    darray=[0 for i in range(0,edatacount)]
    edata=tbl_electionapply.objects.filter(election_position__election_position="President",status__gt=2,election_name=eata)
    j=0
    for i in edata:
        counts=tbl_voting.objects.filter(election_apply=i.id).count()
        #print(counts)
        countarray[j]=counts
        darray[j]=counts
        j=j+1
    
    datas=zip(edata,countarray) 
    #print(edatacount)
    
    return render(request,"Admin/presidentvotings.html",{'data':datas})

def secretarylist(request):
    cdate=date.today()
    electiondata=tbl_electiondeclaration.objects.get(status=0,result_date=cdate)
   
    eata=tbl_electiondeclaration.objects.filter(status=0,result_date=cdate).last()
    edatacount=tbl_electionapply.objects.filter(election_position__election_position="Secretary",status__gt=2,election_name=eata).count()
        
    countarray=[0 for i in range(0,edatacount)] 
    darray=[0 for i in range(0,edatacount)]
    edata=tbl_electionapply.objects.filter(election_position__election_position="Secretary",status__gt=2,election_name=eata)
    j=0
    for i in edata:
        counts=tbl_voting.objects.filter(election_apply=i.id).count()
        #print(counts)
        countarray[j]=counts
        darray[j]=counts
        j=j+1
    
    datas=zip(edata,countarray) 
    #print(edatacount)
    
    return render(request,"Admin/secretaryvotings.html",{'data':datas})

def treasurerlist(request):
    cdate=date.today()
    electiondata=tbl_electiondeclaration.objects.get(status=0,result_date=cdate)
   
    eata=tbl_electiondeclaration.objects.filter(status=0,result_date=cdate).last()
    edatacount=tbl_electionapply.objects.filter(election_position__election_position="Treasurer",status__gt=2,election_name=eata).count()
        
    countarray=[0 for i in range(0,edatacount)] 
    darray=[0 for i in range(0,edatacount)]
    edata=tbl_electionapply.objects.filter(election_position__election_position="Treasurer",status__gt=2,election_name=eata)
    j=0
    for i in edata:
        counts=tbl_voting.objects.filter(election_apply=i.id).count()
        #print(counts)
        countarray[j]=counts
        darray[j]=counts
        j=j+1
    
    datas=zip(edata,countarray) 
    #print(edatacount)
    
    return render(request,"Admin/treasurervotings.html",{'data':datas})


def scholarshipreport(request,sid):
    data=tbl_scholarshipname.objects.get(id=sid)
    mdata=tbl_memberadding.objects.all()
    marr=[]
    for i in mdata:
        marr.append(i.id)
    rdata=tbl_relatives.objects.all()
    rarr=[]
    for i in rdata:
        rarr.append(i.id)
    if request.method=="POST":
        if request.POST.get('fdate')!="" and request.POST.get('edate'):
            datas=tbl_scholarshipapply.objects.filter(scholarship_name=data,member_name__in=marr,status=3,apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
            data=tbl_scholarshipapply.objects.filter(scholarship_name=data,relative_name__in=rarr,status=3,apply_date__gte=request.POST.get('fdate'),apply_date__lte=request.POST.get('edate'))
            return render(request,"Admin/scholarshipreport.html",{'data':datas,'data1':data})
        elif request.POST.get('fdate')!="":
            datas=tbl_scholarshipapply.objects.filter(scholarship_name=data,member_name__in=marr,status=3,apply_date__gte=request.POST.get('fdate'))
            data=tbl_scholarshipapply.objects.filter(scholarship_name=data,relative_name__in=rarr,status=3,apply_date__gte=request.POST.get('fdate'))
            return render(request,"Admin/scholarshipreport.html",{'data':datas,'data1':data})
        else:
            datas=tbl_scholarshipapply.objects.filter(scholarship_name=data,member_name__in=marr,status=3,apply_date__lte=request.POST.get('edate'))
            data=tbl_scholarshipapply.objects.filter(scholarship_name=data,status=3,relative_name__in=rarr,apply_date__lte=request.POST.get('edate'))
            return render(request,"Admin/scholarshipreport.html",{'data':datas,'data1':data})
    else:
        return render(request,"Admin/scholarshipreport.html")

def resetpassword(request,mcid):
    if request.method=="POST":
        mdata=tbl_memberadding.objects.get(id=mcid)
        if request.POST.get('newpass')==request.POST.get('conpass'):
            mdata=tbl_memberadding.objects.get(id=mcid)
            mdata.password=request.POST.get('newpass')
            mdata.save()
            return redirect("Admin:homepage")
        else:
            return render(request,"Admin/resetmemberprofile.html")
    else:
        return render(request,"Admin/resetmemberprofile.html")


