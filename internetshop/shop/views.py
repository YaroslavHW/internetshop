from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home():
    return HttpResponse("<h1>Internet Shop</h1> Some description")