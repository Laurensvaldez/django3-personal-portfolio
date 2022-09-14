from django.shortcuts import render
# import the model from the project
from .models import Project

# Create your views here.


def home(request):
    # this grabs all the projects from the database
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
