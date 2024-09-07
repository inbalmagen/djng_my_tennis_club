from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def members(request):
    template = loader.get_template('members_page.html')
    return HttpResponse(template.render())

def trainers(request):
    template = loader.get_template('trainers_page.html')
    return HttpResponse(template.render())

def courts(request):
    template = loader.get_template('courts_page.html')
    return HttpResponse(template.render())


def main(request):
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render())
    # return HttpResponse("Welcome to my main page!")

