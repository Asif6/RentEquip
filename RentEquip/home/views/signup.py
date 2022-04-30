from django import views
import django

from django.shortcuts import render
from home.forms import SignupForm
from home.models.nuser import Nuser
import uuid
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
import traceback
from django.contrib import messages

def send_signup_mail(request,email,token,name):
    current_site=get_current_site(request)

    subject="Email verifications"
    message=f" Hi {name} To verify your account please click the link {current_site}/{token}"
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email]
    fail_silently=False

    send_mail(subject,message,from_email,recipient_list,fail_silently)







class Signup(views.View):

    def get(self,request):

        form= SignupForm()
        # form.order_fields(field_order=["first_name",'last_name','userName','email','password'])
        data={}
        data["form"]=form
        return render(request,"home/signup.html",data)
    def post(self,request):

        data={}

        error=None

        form=SignupForm(request.POST)
        data['form']=form


        if form.is_valid():

            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data["last_name"]
            userName=form.cleaned_data['userName']
            email=form.cleaned_data["email"]
            password=form.cleaned_data['password1']
            fullname=str(first_name)+' '+str(last_name) 

            token=uuid.uuid4()
            user=Nuser(first_name=first_name,last_name=last_name,userName=userName,email=email,password=password,token=token)
            
            try:
                send_signup_mail(request,email=email,token=token,name=fullname)
                user.save()
                messages.success(request,"Your Account created successfully... Please chake your email to verify your account ")
            
            except Exception as e:

                messages.error(request, 'Internal Server Error Try Later')
                # print('BAWWWWWWWWWWWWWWWWW',error)

            data['error']=error  
            data["user"]=user

            return render(request,"home/signup.html",data)


        return render(request,"home/signup.html",data)