from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    latest_question_list= Question.objects.order_by("-pub_date")[:7]
    context={
        "latest_question_list":latest_question_list,
    }
    return render(request,"polls/index.html",context)

def details(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/details.html",{"question":question})

def results(request):
    return render(request,'polls/results.html')

def votes(request,question_id):
    return HttpResponse("Finally ypur votes!")