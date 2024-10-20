from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,get_object_or_404

def index(request):
    return render(request,'polls/index.html')

def details(request):
    return render(request,'polls/details.html')

def results(request):
    return render(request,'polls/results.html')

def votes(request,question_id):
    return HttpResponse("Finally ypur votes!")