from Guest import views
from django.urls import path
app_name='Guest'
urlpatterns = [
    path('newuser/', views.newuser,name="newuser"),
    path('ajaxplace/',views.ajaxplace,name="Ajaxplace"),
    path('login/', views.login,name="login"),
     path('', views.index,name="index"),
     path('fpass/', views.ForgetPassword,name="forpass"),
    path('otpver/', views.OtpVerification,name="verification"),
    path('create/', views.CreateNewPass,name="create"),
    path('ajaxemail/', views.ajaxemail,name="ajaxemail"),
    
]