from django.urls import path
from . import views

urlpatterns=[
    path('', views.index,name='index'),	
    path('about/', views.about,name='about'),
    path('hello/<str:username>', views.hello,name='hello'),	
    path('projects/', views.projects,name='projects'),
    path('projects/<int:id>', views.projects_details,name='projects_details'),
    path('tasks/', views.tasks,name='tasks'),
    path('create_task/', views.create_task,name='create_task'),
    path('create_proyect/', views.create_proyect,name='create_proyect'),
]