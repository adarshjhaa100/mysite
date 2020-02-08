from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Choice
# Create your views here.

def index(request):
    print(Question.objects.all())
    return HttpResponse(f'This is index page')

def addQuestion(request):
    if(Question.objects.all().count()==0):
        for i in range(5):
            q=Question(questionText=f'This is question#{i+1}')
            q.save()
    print('count of question',len(Question.objects.all()))    

    for i in Question.objects.all():
        for j in range(4):
            i.choice_set.create(text=f'Choice#{j+1}for question:{i.id}')
        i.save()
    print(Choice.objects.all())        
    return HttpResponse(f'question added')