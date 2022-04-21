from django import views

from django.shortcuts import render
from home.forms import LoginForm

class Login(views.View):
    def get(self,request):

        form=LoginForm()

        data={}
        data["form"]=form
        

        return render(request,"home/login.html",data)