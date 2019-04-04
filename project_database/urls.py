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
from django.http import HttpResponse, JsonResponse, QueryDict
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


    def users(request):
        if request.method == "GET":
            data = {}
            for usr in User.objects.all():
                data[usr.id] = str(usr.display_name) + " (@" + str(usr.username) + ")"
            return JsonResponse(data)
        elif request.method == "POST":
            data = QueryDict(request.META["QUERY_STRING"]).dict()
            # data = json.loads(request.body.decode("utf-8"))
            print(data)
            User.objects.create(id=data["id"], display_name=data["display_name"], username=data["username"], longitude=data["longitude"], latitude=data["latitude"])
            response = {"Message":"OK (200)"}
            return JsonResponse(response)

    def modify(request, user_id):
        if request.method == "PATCH":
            data = QueryDict(request.META["QUERY_STRING"]).dict()
            usr = User.objects.get(id=user_id)
            for (key, value) in data.items():
                setattr(usr, key, value)
            usr.save()
            response = {"Message":"UPDATED (200)"}
            return JsonResponse(response)
        if request.method == "DELETE":
            User.objects.get(id=user_id).delete()
            response = {"Message":"DELETED (200)"}
            return JsonResponse(response)

    def locations(request):
        data = {}
        for usr in User.objects.all():
            data[usr.id] = userInfo.aoi(request,usr.username)
        return JsonResponse(data)

urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('<str:usrname>/poi', userInfo.aoi, name='poi'),
    path('users/', userInfo.users, name = "users"),
    path('users/<int:user_id>', userInfo.modify, name="modify"),
    path('locations/',userInfo.locations, name = "locations")

]
