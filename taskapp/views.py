from django.shortcuts import render, get_object_or_404
from django.utils  import timezone
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models  import Task, Category

# Create your views here.
def homepage(request):
    tasks = Task.objects.all()
    return render(request, 'taskapp/home.html',{'tasks':tasks})


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
        


class TaskCreate(CreateView):
    model=Task
    fields=['title', 'description', 'completed', 'category']
    success_url = reverse_lazy('category_list')


class TaskUpdate(UpdateView):
    model=Task
    fields=['title', 'description', 'completed']   
    success_url = reverse_lazy('category_list')

class TaskDelete(DeleteView):
    model=Task
    context_object_name='task'
    success_url = reverse_lazy('category_tasks')
    
def CategoryList(request):
    categories = Category.objects.all()
    return render(request, 'taskapp/category_list.html', {'categories':categories})


class CategoryCreate(CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('category_list')


class CategoryDelete(DeleteView):
    model = Category
    context_object_name='task'
    success_url = reverse_lazy('category_list')

def category_tasks(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    tasks=category.task_set.all()
    return render(request, 'taskapp/home.html',{'category':category, 'tasks':tasks})


def task_chart(request):
    categories = Category.objects.all()
    pending_counts={}
    for category in categories:
        pending_counts[category.name] = Task.objects.filter(
            category=category,
            date_created__gt= timezone.now()
        ).count()    
    return render(request, 'taskapp/task_chart.html', {'pending_counts':pending_counts})    
    

