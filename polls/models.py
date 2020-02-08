from django.db import models

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.questionText
    questionText=models.CharField(max_length=200,default='')

class Choice(models.Model):
    def __str__(self):
        return self.text
    que=models.ForeignKey(Question,on_delete=models.CASCADE)
    text=models.CharField(max_length=100,default='q')
    votes=models.IntegerField(default=0)    