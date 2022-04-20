from django import views

from django.shortcuts import render


class Signup(views.View):

    def get(self,request):
        return render(request,"home/signup.html")


