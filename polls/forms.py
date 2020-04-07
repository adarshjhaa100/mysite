from django import forms

class NameForm(forms.Form):
    yourName=forms.CharField(max_length=200,label='name')

class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 100)  
    
class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(required=False,label='Your e-mail address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
