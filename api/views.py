from django.shortcuts import render
from  django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SerializersTask
from .models import Task
# Create your views here.

@api_view(['GET'])
def apiOVerview(request):
    api_url = {
        'list' : '/task-list',
        'detail': '/task/detail/<str:pk>',
        'create': '/task/create'
        }
    return Response(api_url)

@api_view(['GET'])
def taskList(request):
    task = Task.objects.all()
    serializer = SerializersTask(task, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detailTask(request, pk):
    detail = Task.objects.get(pk = pk)
    serializer = SerializersTask(detail)
    return Response(serializer.data)

@api_view(['POST'])
def createTask(request):
    serlizer = SerializersTask(data=request.data)
    if serlizer.is_valid():
        serlizer.save()
    else:
        print("fail")
    return Response(serlizer.data)

@api_view(['PUT'])
def updateTask(request, pk):
    task = Task.objects.get(pk = pk)
    serializer = SerializersTask(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = SerializersTask(instance=task)
    task.delete()
    return Response('done ')

def home(request):
    context = {}
    return render(request, 'home.html', context)