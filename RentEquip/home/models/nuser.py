import email
from lib2to3.pgen2 import token
from tkinter.tix import Tree
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models



class MyuserManager(BaseUserManager):

    use_in_migrations=True

    def create_user(self,first_name,last_name,email,password,**extra_fields):

        if not first_name:
            raise ValueError("First Name is required")
        if not last_name:
            raise ValueError("Last Name is required")
        if not email:
            raise ValueError("Email is required")

        email=self.normalize_email(email=email)
        user=self.model(first_name=first_name,last_name=last_name,email=email,password=password,**extra_fields)
        user.set_password(raw_password=password)
        user.save(using=self._db)
        return user
    

    
    
    def create_superuser(self,first_name,last_name,email,password,**extra_fields):

        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_admin',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff',True)

        return self.create_user(first_name,last_name,email,password,**extra_fields)
        




class Nuser(AbstractBaseUser,PermissionsMixin):

    first_name= models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    userName=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)

    token=models.CharField(max_length=500)
    is_email_verify=models.BooleanField(default=False)

    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    objects=MyuserManager()

    REQUIRED_FIELDS = ['first_name','last_name']
    USERNAME_FIELD="email"
   

    def __str__(self):
        return self.email


