import re
from django.urls import path, include
from . import views
from django.conf.urls import url
from .models import Album
app_name="music"

urlpatterns = [
    path("", views.index, name="index"),
    #   path("music/",views.detail,name="detail"),
    path('music/<int:album_id>/', views.detail, name="detail"),

]
