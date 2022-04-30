from django.urls import path
from .views.index import Index
from .views.signup import Signup
from .views.login import Login
from .views.emailconfirm import EmailConfirmView
urlpatterns=[
    path("",Index.as_view(),name="index"),
    path("signup/",Signup.as_view(),name="signup"),
    path("login/",Login.as_view(),name="login"),
    path("confirm-email",EmailConfirmView.as_view(),name="confirmemail")
]