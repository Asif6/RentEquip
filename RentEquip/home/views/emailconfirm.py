from django import views
from django.shortcuts import redirect,render

class EmailConfirmView(views.View):

    def get(self,request):
        return render(request,"home/emailconfirmation.html") 