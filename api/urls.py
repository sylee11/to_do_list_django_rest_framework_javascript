from django.urls import include,path
from . import views

urlpatterns = [
    path('', views.apiOVerview, name="api-overview"),
    path('task-list', views.taskList, name="views-all-task"),
    path('task/detail/<int:pk>', views.detailTask, name="views-detail-task"),
    path('task/create', views.createTask, name="views-create-task"),
    path('task/update/<int:pk>', views.updateTask, name="views-update-task"),
    path('task/delete/<int:pk>', views.deleteTask, name="views-delete-task"),
    path('home', views.home, name='home')
]