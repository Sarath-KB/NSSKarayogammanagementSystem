
from Admin import views
from django.urls import path
app_name='Admin'
urlpatterns = [
    path('district/', views.district,name="district"),
    path('category/',views.category,name="category"),
    path('deldid/<int:did>',views.deldis,name="deldis"),
    path('delete_category/<int:cid>',views.delcat,name="delcat"),
    path('edit_district/<int:did>',views.disedit,name="disedit"),
    path('edit_category/<int:cid>',views.catedit,name="catedit"),
    path('place/',views.place,name="place"),
    path('delplace/<int:pid>',views.deleteplace,name="deleteplace"),
    path('subcategory/',views.subcategory,name="subcategory"),
    path('delsubcat/<int:scatid>',views.deletesubcat,name="deletesubcat"), 
    path('memberadding/', views.memberadding,name="memberadding"),
    path('ajaxlocation/',views.ajaxlocation,name="Ajaxlocation"),   
    path('financehead/',views.financehead,name="financehead"),
    path('scheme/',views.scheme,name="scheme"),
    path('deletefinancehead/<int:fhid>',views.deletefinancehead,name="deletefinancehead"),
    path('edit_financehead/<int:fhid>',views.editfinancehead,name="editfinancehead"),
    path('deletescheme/<int:sid>',views.deletescheme,name="deletescheme"),
    path('edit_scheme/<int:sid>',views.editscheme,name="editscheme"),
    path('deletemember/<int:mid>',views.deletemember,name="deletemember"),
    path('loan/',views.loan,name="loan"),
    path('deleteloan/<int:lid>',views.deleteloan,name="deleteloan"),
    path('edit_loan/<int:lid>',views.editloan,name="editloan"),
    path('admin_homepage/',views.homepage,name="homepage"),
    path('proof/',views.proof,name="proof"),
     path('deleteproof/<int:pid>',views.deleteproof,name="deleteproof"),
     path('edit_proof/<int:pid>',views.editproof,name="editproof"),
    path('relationtype/',views.relationtype,name="relationtype"),
    path('delete_relationtype/<int:rid>',views.deleterelationtype,name="deleterelationtype"),
     path('edit_relationtype/<int:rid>',views.editrelationtype,name="editrelationtype"),
     path('scholarshiptype/',views.scholarshiptype,name="scholarshiptype"),
      path('delete_scholarshiptype/<int:sid>',views.deletescholarshiptype,name="deletescholarshiptype"),
     path('scholarshipname/',views.scholarshipname,name="scholarshipname"),
    path('delete_scholarshipname/<int:snid>',views.deletescholarshipname,name="deletescholarshipname"),
    path('viewscholarshipapplications/',views.scholarshipapplications,name="scholarshipapplications"),
    path('scholarshipaccept/<int:said>', views.scholarshipaccept,name="scholarshipaccept"),
    path('scholarshipreject/<int:srid>', views.scholarshipreject,name="scholarshipreject"),
    path('scholarshipacceptlist/', views.scholarshipacceptlist,name="scholarshipacceptlist"),
#    path('scholarshipgrant/<int:sgid>', views.scholarshipgrant,name="scholarshipgrant"),
    path('scholarshiprejectlist/', views.scholarshiprejectlist,name="scholarshiprejectlist"),
    path('mlist/', views.mlist,name="mlist"),
    path('rlist/<int:mid>', views.rlist,name="rlist"),
    # path('memberdelete/<int:mdid>', views.memberdelete,name="memberdelete"),
    path('electionposition/', views.electionposition,name="electionposition"),
     path('delete_electionposition/<int:eid>',views.deleteelectionposition,name="deleteelectionposition"),
     path('electiondeclaration/', views.electiondeclaration,name="electiondeclaration"),
     path('electiondeclarationdelete/<int:edid>',views.electiondeclarationdelete,name="electiondeclarationdelete"),
    path('electionapplication/', views.electionapplication,name="electionapplication"),
    path('electionapplyaccept/<int:eaid>', views.electionapplyaccept,name="electionapplyaccept"),
    path('electionapplyreject/<int:erid>', views.electionapplyreject,name="electionapplyreject"),
    path('electionapplyacceptlist/', views.electionapplyacceptlist,name="electionapplyacceptlist"),
     path('viewvote/', views.viewvote,name="viewvote"),
    path('presidentvotings/', views.presidentvotings,name="presidentvotings"),
     path('secretaryvotings/', views.secretaryvotings,name="secretaryvotings"),
    path('treasurervotings/', views.treasurervotings,name="treasurervotings"),
    path('events/', views.events,name="events"),
    path('deleteevents/<int:enid>', views.deleteevents,name="deleteevents"),
    path('logout/', views.logout,name="logout"),
    path('prelist/', views.presidentlist,name="prelist"),
    path('secretarylist/', views.secretarylist,name="secretarylist"),
    path('treasurerlist/', views.treasurerlist,name="treasurerlist"),
    path('scholarshipreport/<int:sid>', views.scholarshipreport,name="scholarshipreport"),
    path('passedmember/<int:mid>',views.passedmember,name="passedmember"),
 path('resetpassword/<int:mcid>',views.resetpassword,name="resetpassword"),

    

]

