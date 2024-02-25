from django.urls import path
from . import views

urlpatterns = [
    path('', views.real, name="real"),
    path('aboutpage', views.aboutpage, name="aboutpage"),
    path('registerdata', views.registerdata, name="registerdata"),
    path('contactpage', views.contactpage, name="contactpage"),
    path('storedata', views.storedata, name="storedata"),
]