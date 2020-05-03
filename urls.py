"""SandhyaProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: fromv django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login',views.loginUser,name='login'),
    url(r'^donaterRegistration$',views.donatorReg,name='dreg'),
    url(r'^logout$',views.logoutUser,name='logout'),
    url(r'^orphanageReg$',views.orphanageReg,name='oreg'),
    url(r'^thingdonation$',views.thingDonate,name='thingdonate'),
    url(r'^profile$',views.profile,name='profile'),
]
