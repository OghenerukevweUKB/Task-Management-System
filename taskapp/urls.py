from django.urls import path
from . views import *
from . import views 

urlpatterns = [
    path('category_tasks', views.homepage, name='category_tasks'),
    path('task/<int:pk>/', TaskDetail. as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task-chart/',views.task_chart, name='task_chart'),
    path('', views.CategoryList, name='category_list'),
    path('categories/create/', CategoryCreate.as_view(), name='create_category'),
    path('categories/<int:category_id>/', views.category_tasks, name='category_tasks'),
    path('categories/delete/<int:pk>/', CategoryDelete.as_view(), name='delete_category')
    
]
