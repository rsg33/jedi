from django.urls import path
from . import views

app_name = 'hr'

urlpatterns = [
    path('', views.main_list, name='main_list'),
    path('candidate', views.candidate_create, name='candidate_create'),
    path('questions', views.questions, name='questions'),
    path('tested', views.tested, name='tested'),
    path('jedi', views.jedi_list, name='jedi_list'),
    path('candilist', views.candidate_list, name='candidate_list'),
    path('inpadavan', views.inpadavan, name='inpadavan'),
]
