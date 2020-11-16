from django.urls import path
from .views import *

urlpatterns = [
    path('task/', TaskListView.as_view()),
    path('task/<int:task_id>', TaskDetailsView.as_view()),
    path('create_task/', CreateTaskView.as_view())
]
