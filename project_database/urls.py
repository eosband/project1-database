"""project_database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.urls import include, path
from rest_framework import routers
from SQLapp import views
from SQLapp.models import *


class userInfo(View):

    def aoi(request, usrname):
        data = {}
        personal_id = User.objects.get(username=usrname).id
        for location in Location.objects.filter(userID=personal_id):
            data[location.place_title] = (float(location.latitude), float(location.longitude))
        return JsonResponse(data)
        # temp = User.objects.get(username=usrname).display_name
        # return HttpResponse(temp)


urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('<str:usrname>/poi', userInfo.aoi, name='poi')
]
