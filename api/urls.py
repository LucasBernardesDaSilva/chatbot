from django.conf.urls import url
from django.urls import path, re_path
from api import views

urlpatterns = [
    path('event/', views.event),
    re_path(r'^user/(?P<user_id>\d+)$',views.exibir, name="exibir"),
]