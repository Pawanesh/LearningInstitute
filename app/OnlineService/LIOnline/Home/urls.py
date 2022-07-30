from django.urls import path

from Home.views import HomeView, HomeClassView, HomeSubjectClassView

urlpatterns = [
    path('', HomeView.as_view(), name='HomeView'),
    path('class', HomeClassView.as_view(), name='HomeClassView'),
    path('class/<int:subjectid>/', HomeSubjectClassView.as_view(), name='HomeSubjectClassView'),
]