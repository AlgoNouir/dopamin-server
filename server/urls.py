from django.contrib import admin
from django.urls import path
from core.views import MainData,Factor


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", MainData.as_view(), name="main"),
    path("factor/<int:factorID>", Factor.as_view(), name="main"),
]