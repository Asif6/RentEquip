from django import views

from django.shortcuts import render

class Index(views.View):

    def get(self,request):
        return render(request,'home/index.html')