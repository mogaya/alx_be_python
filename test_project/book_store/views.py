from django.shortcuts import render
from django.http import HttpResponse

def index(request): return HttpResponse("Welcome To my Book Store!!")

# Create your views here.