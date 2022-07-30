from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.template import loader

import requests

class HomeView(View):
    def get(self, request):
        context = {}
        subject = requests.get("http://127.0.0.1:8000/subject")
        if subject.status_code == 200:
            context = subject.json()
        return render(request, 'home.html', context)

class HomeClassView(View):
    def get(self, request):
        context = {}
        classData = requests.get("http://127.0.0.1:8000/class")
        if classData.status_code == 200:
            context = classData.json()
        
        print(context)
        return render(request, 'home_class.html', context)
    
class HomeSubjectClassView(View):
    def get(self, request, subjectid):
        print("Requesting class info for subject: {}".format(subjectid))
        context = {}
        classData = requests.get("http://127.0.0.1:8000/class", params = {'SubjectID':subjectid})
        if classData.status_code == 200:
            context = classData.json()
        
        print(context)
        return render(request, 'home_class_subject.html', context)    