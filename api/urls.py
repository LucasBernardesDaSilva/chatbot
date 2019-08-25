from django.conf.urls import url
from django.urls import path, re_path
from api import views

urlpatterns = [
    path('event/', views.event),
]