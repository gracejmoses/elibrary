from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def welcome(request):
    # return HttpResponse("Welcom to e-library")
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def books(request):
    # return HttpResponse("Books")
    template = loader.get_template('books.html')
    return HttpResponse(template.render())

def users(request):
    # return HttpResponse("users")
    template = loader.get_template('users.html')
    return HttpResponse(template.render())
