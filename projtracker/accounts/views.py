from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import ProjectNames,UserTasks
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# Create your views here.


def indexView(request):
    return render(request,'index.html')

@login_required
def dashboardView(request):
    list_of_projects = ProjectNames.objects.all()
    if request.user.is_authenticated:
            print(request.user.id)
            username = User.objects.get(id=request.user.id)
            list_of_task = UserTasks.objects.values('id','Task_title','start_time','end_time','status').all().filter(employee=username)
            print(list_of_task)
    if request.method == "POST":
        if request.POST.get('start'):
            selected_project = get_object_or_404(ProjectNames,pk=request.POST.get('project_id'))
            print(selected_project)
            print(request.POST.get('name'))
            print(request.POST.get('start'))
            
            task = UserTasks()
            task.employee = username
            task.Task_title = request.POST.get('name')
            task.start_time = request.POST.get('start')
            task.save()
        else:
            print(request.POST.get('end'))
            data = request.POST.get('end')
            if data:
                id, date = data.split(',')
                task = UserTasks.objects.get(id=id)
                task.end_time = date
                task.status = False
                task.save()

        
    return render(request,'dashboard.html',{'projects':list_of_projects,'tasks':list_of_task})

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})

