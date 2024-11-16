from django.utils import timezone
from django.http import HttpResponseRedirect,HttpResponse
from django.db.models import F
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404

from polls.forms import NameForm
from .models import Question,Choice

def index(request):
    latest_question_list= Question.objects.order_by("-pub_date")
    context={
        "latest_question_list":latest_question_list,
    }
    return render(request,"polls/index.html",context)

def details(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/details.html",{"question":question})

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{"question":question})

def vote(request,question_id):
    print("vote")
    question=get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request,"polls/details.html",
            {
                "question":question,
                "error_message":"You didn't select a choice.",
            },
        )
    else:
        # print(selected_choice)
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results",args=(question.id,))) 
    
def add_question(request):
    if request.method == 'POST':
        question_text=request.POST.get('question_text')
        choice1=request.POST.getlist('choice1')
       
        # print(choice1)
        if question_text:
            question=Question.objects.create(question_text=question_text,pub_date=timezone.now())
            for values in choice1:
                Choice.objects.create(question=question,choice_text=values,votes=0)
                
            question.save()
            return redirect('polls:index')
        else:
            return render(request, 'polls/add_question.html',{
                'error_message':"All fields ae required."
            })
    return render(request,'polls/add_question.html')

def delete_question(request,question_id):
    question=Question.objects.filter(pk=question_id).delete()
    return redirect('polls:index')

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse("polls:thanks"))
    else:
        form = NameForm()
    
    return render(request,"polls/name.html",{"form":form})

def thanks(request):
    return HttpResponse("<h3> Thanks for your Contribution.<h3>")

# def login_page(request):
#     if request.m