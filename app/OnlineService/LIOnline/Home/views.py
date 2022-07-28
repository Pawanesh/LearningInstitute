from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.template import loader

class HomeView(View):
    def get(self, request):
        num_books = 5
        num_instances = 4
        num_instances_available = 4
        num_authors = 5
        context = {
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            }

        return render(request, 'home.html', context)
    
    