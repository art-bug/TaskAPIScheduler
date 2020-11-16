from django.shortcuts import render
from .tasks import *

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import *

# Create your views here.

def index(request):
    task_list = Task.objects.all()
    return render(request, "task_processing_api/index.html", context={'tasks': task_list})

def process_task(task_type, name, description):
    new_task = Task.objects.create(task_type=task_type,
                                   name=name,
                                   description=description)

    print("Created task with ID", str(new_task.task_id) + ":", task_type, name, description, '\n')

    if task_type == 'A':
        agent_a.delay(new_task.pk)
        print("Agent A start processing task A with ID", new_task.task_id,'\n')
    elif task_type == 'B1' or task_type == 'B2':
        agent_b.delay(new_task.pk)
        print("Agent B start processing task", task_type, "with ID", new_task.task_id,'\n')

class TaskListView(APIView):
    def get(self, request):
        task_list = Task.objects.all()
        serializer = TaskListSerializer(task_list, many=True)
        return Response(serializer.data)

class CreateTaskView(APIView):
    def post(self, request):
        new_task = CreateTaskSerializer(data=request.data)
        if new_task.is_valid():
            new_task.save()
            task_type = new_task.data["task_type"]
            task_name = new_task.data["name"]
            task_description = new_task.data["description"]
            process_task(task_type, task_name, task_description)
        return Response(status=201)

class TaskDetailsView(APIView):
    def get(self, request, task_id):
        task = Task.objects.get(task_id=task_id)
        serializer = TaskDetailsSerializer(task)
        return Response(serializer.data)
