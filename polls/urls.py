from django.urls import path
from . import views

app_name='polls'

urlpatterns=[
    path('',views.index,name='index'),
    path('addQuestion/',views.addQuestion,name='addQuestion'),
    path('<int:questionId>/',views.detail,name='detail'),
    path('<int:question_id>/results/',views.results,name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
    path('formSample/',views.get_name,name='sample'),
    path('contacts/',views.contact,name='contact')
    
]