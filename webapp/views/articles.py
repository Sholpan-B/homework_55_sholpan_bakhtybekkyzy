from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'task_create.html')
    task_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'details': request.POST.get('details'),
        'deadline': request.POST.get('deadline'),
        'status': request.POST.get('status'),
    }
    task = Task.objects.create(**task_data)
    return redirect('task_detail', pk=task.pk)


def update_view(request: WSGIRequest, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        deadline = str(task.deadline)
        return render(request, 'task_update.html', context={'task': task, 'deadline': deadline, 'status': task.status})
    deadline = None
    if request.POST.get('deadline'):
        deadline = request.POST.get('deadline')
    task.title = request.POST.get('title'),
    task.description = request.POST.get('description'),
    task.details = request.POST.get('details'),
    task.deadline = deadline
    task.status = request.POST.get('status'),
    task.save()
    return redirect('task_detail', pk=task.pk)


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={
        'task': task
    })


def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')
