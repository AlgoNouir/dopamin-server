from django.contrib import admin
from django.urls import path
from core.views import MainData


urlpatterns = [
path("admin/", admin.site.urls, name="admin"),
path("", MainData.as_view(), name="main"),
]