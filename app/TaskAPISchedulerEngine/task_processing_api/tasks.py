from celery import shared_task
from time import sleep
from datetime import datetime
from .models import *

@shared_task
def agent_a(task_a_pk):
    task_a = Task.objects.get(pk=task_a_pk)
    task_a.status = "Executing"
    task_a.save()
    print("Task A with ID", task_a.task_id, "assigned Executing status.", '\n')

    print("Agent A with task ID", task_a.task_id, "go to sleep for 3 seconds", '\n')
    sleep(3)

    new_task_b1 = Task.objects.create(task_type="B1")
    new_task_b1.save()
    print("Created task with ID", str(new_task_b1.task_id) + ":", new_task_b1.task_type, '\n')

    print("Agent B start processing task", new_task_b1.task_type, "with ID", new_task_b1.task_id, '\n')
    agent_b.delay(new_task_b1.pk)

    print("Agent B with task ID", new_task_b1.task_id, "go to sleep for 3 seconds", '\n')
    sleep(3)

    new_task_b2 = Task.objects.create(task_type="B2")
    new_task_b2.save()
    agent_b.delay(new_task_b2.pk)
    print("Created task with ID", str(new_task_b2.task_id) + ":", new_task_b2.task_type, '\n')

    task_a.status = "Executed"
    task_a.save()
    print("Task A with ID", task_a.task_id, "assigned Executed status.", '\n')

    return task_a.status

@shared_task
def agent_b(task_b_pk):
    task_b = Task.objects.get(pk=task_b_pk)
    task_b.status = "Executing"
    task_b.save()
    print("Task B with ID", task_b.task_id, "assigned Executing status.", '\n')

    print("Agent B with task ID", task_b.task_id, "go to sleep for 5 seconds", '\n')
    sleep(5)

    print("Creation of the result and its content.", '\n')
    result_content = '{current_time}, задача№{task_id}'.format(
                      current_time=datetime.now().time(),
                      task_id=task_b.task_id)
    result = Result.objects.create(result_id=task_b, content=result_content)
    result.save()

    task_b.status = "Executed"
    task_b.save()
    print("Task B with ID", task_b.task_id, "assigned Executed status.", '\n')

    return task_b.status
