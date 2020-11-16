from rest_framework import serializers

from .models import Task


class TaskListSerializer(serializers.ModelSerializer):
    ''' Get task list. '''

    class Meta:
        model = Task
        fields = ('task_id', 'task_type', 'name', 'description', 'status')


class CreateTaskSerializer(serializers.ModelSerializer):
    ''' Post new task. '''

    class Meta:
        model = Task
        fields = ('task_type', 'name', 'description')


class TaskDetailsSerializer(serializers.ModelSerializer):
    ''' Get task details. '''

    class Meta:
        model = Task
        fields = ('task_type', 'name', 'description', 'status')
