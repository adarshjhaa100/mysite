from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from .forms import NameForm,StudentForm
from django import forms
# Create your views here.

def index(request):
    print(Question.objects.all())
    a=Question.objects.all()
    output=', '.join([i.questionText for i in a])
    context={
        'queList':a
    }

    #return HttpResponse(f'This is index page{output}')
    return render(request,'polls/index.html',context)

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

def detail(request,questionId):
    # try:
    #     question=Question.objects.get(pk=questionId)
         
    # except Question.DoesNotExist:
    #     raise Http404('Doesnt Exist') 
    question = get_object_or_404(Question, pk=questionId)   
    return render(request,'polls/details.html',{'question':question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


#handling forms

def get_name(request):
    # if(request.method=='post'):
    #     form=NameForm(request.POST)
    #     if(form.is_valid()):
    #         print(form.cleaned_data)
            
    # else:
    #     form=NameForm()
    student = StudentForm(request.POST)  
    ad=''
    if(student.is_valid()):
        ad=student.cleaned_data
        print(ad)
        return HttpResponseRedirect('/polls/formSample')
    print(ad)    
    return render(request,"polls/name.html",{'form':student})      
        
class ContactForm(forms.Form):
     yourname = forms.CharField(max_length=100, label='Your Name')
     email = forms.EmailField(required=False,label='Your e-mail address')
     subject = forms.CharField(max_length=100)
     message = forms.CharField(widget=forms.Textarea)
 
 
def contact(request):
     submitted = False
     if request.method == 'POST':
         form = ContactForm(request.POST)
         if form.is_valid():
             cd = form.cleaned_data
             print(cd)
             # assert False
             return HttpResponseRedirect('/polls/contacts')
     else:
         form = ContactForm()
         if 'submitted' in request.GET:
             submitted = True
 
     return render(request, 'polls/contact.html', {'form': form, 'submitted': submitted})
