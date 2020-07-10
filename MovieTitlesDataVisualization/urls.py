from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajaxResponse', views.ajaxResponse, name='ajaxResponse'),
]
