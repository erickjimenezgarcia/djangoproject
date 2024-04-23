from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title='Django Course !!'
    return render(request, 'index.html',{
        'title':title
    })

def about(request):
    username='erick';
    return render(request, 'about.html',{
        'username':username
    })

def hello(request, username):    
    return HttpResponse('<h1>Hello %s</h1> ' % username)

def projects(request):
    #projects=list(Project.objects.values())
    projects=Project.objects.all()
    return render(request, 'projects/projects.html',{
        'projects':projects
    })
    

def tasks(request):
    #task=Task.objects.get(title=title)
    tasks=Task.objects.all()
    return render(request, 'tasks/tasks.html',{
        'tasks':tasks
    })    

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask
        })
    else:     
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project_id=2,            
        )
        return redirect('tasks')

def create_proyect(request):
    if request.method == 'GET':
        return render(request, 'projects/create_proyect.html', {
            'form': CreateNewProject
        })
    else:     
        Project.objects.create(name=request.POST['name'],)        
        return redirect('projects')
    
def projects_details(request, id):
    project=get_object_or_404(Project, id=id)
    tasks=Task.objects.filter(project_id=id)   
    return render(request, 'projects/projects_details.html',{
        'project':project,
        'tasks':tasks
    })