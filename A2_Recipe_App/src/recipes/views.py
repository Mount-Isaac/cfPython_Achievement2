from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

# Create your views here.
def recipes_home(request):
    return render(request, "recipes/recipes_home.html")