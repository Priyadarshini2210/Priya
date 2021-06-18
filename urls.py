from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('<str:slug>', views.read_article),
]
