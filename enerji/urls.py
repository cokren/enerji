"""enerji URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from enerji.views import index
from jenerator.views import jenerator, jengraph1 
from katodik.views import katodik, katodikmodbus, katodikizleme

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('jenerator/', jenerator,name="jenerator"),
    path('jengraph1/', jengraph1,name="jengraph1"),
    path('katodik/', katodik, name="katodik"),
    path('katodikmodbus/', katodikmodbus, name="katodikmodbus"),
    path('katodikizleme/', katodikizleme, name="katodikizleme"),
 
    

]
admin.site.site_header = 'Enerji İşleri Yönetim'
