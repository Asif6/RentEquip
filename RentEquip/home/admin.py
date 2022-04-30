from tkinter import N
from django.contrib import admin

# Register your models here.


from .models.nuser import Nuser

admin.site.register(Nuser)