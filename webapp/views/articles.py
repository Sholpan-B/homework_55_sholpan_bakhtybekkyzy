from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from webapp.forms import TaskForm
from webapp.models import Task, StatusChoice


def add_view(request: WSGIRequest):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'task_create.html',
                      context={
                          'choices': StatusChoice.choices,
                          'form': form
                      })
    form = TaskForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'task_create.html',
                      context={
                          'choices': StatusChoice.choices,
                          'form': form
                      })
    else:
        task = Task.objects.create(**form.cleaned_data)
        return redirect('task_detail', pk=task.pk)


def update_view(request, pk):
    errors = {}
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'GET':
        form = TaskForm(initial={
            'title': task.title,
            'description': task.description,
            'details': task.details,
            'deadline': task.deadline,
            'status': task.status
        })
        return render(request, 'task_update.html',
                      context={
                          'task': task,
                          'choices': StatusChoice.choices,
                          'form': form
                      })
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.details = form.cleaned_data['details']
            task.description = form.cleaned_data['description']
            task.deadline = form.cleaned_data['deadline']
            task.status = form.cleaned_data['status']
            task.save()
            return redirect('task_detail', pk=task.pk)

        else:
            if not request.POST.get('title'):
                errors['title'] = 'Данное поле обязательно к заполнению'
            return render(request, 'task_update.html',
                          context={
                              'task': task,
                              'choices': StatusChoice.choices,
                              'errors': errors,
                              'form': form
                          })


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={
        'task': task
    })


def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_confirm_delete.html', context={'task': task})


def confirm_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')
