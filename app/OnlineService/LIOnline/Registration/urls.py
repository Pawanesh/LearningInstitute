from django.urls import path

from Registration import views

urlpatterns = [
    path('', views.index, name='index'),
]