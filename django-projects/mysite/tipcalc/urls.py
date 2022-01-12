from django.urls import path
from . import views

urlpatterns = [
    path('tip', views.tip, name='tip'),
]
