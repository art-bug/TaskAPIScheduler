from django.db import models

# Create your models here.
class Task(models.Model):
    TYPE_A = "A"
    TYPE_B1 = "B1"
    TYPE_B2 = "B2"
    TASK_TYPE_CHOICES = (
        (TYPE_A, "А"),
        (TYPE_B1, "Б1"),
        (TYPE_B2, "Б2")
    )
    STATUS_CREATED = "Created"
    STATUS_EXECUTING = "Executing"
    STATUS_EXECUTED = "Executed"
    TASK_STATUS_CHOICES = (
        (STATUS_CREATED, "Создана"),
        (STATUS_EXECUTING, "Выполняется"),
        (STATUS_EXECUTED, "Выполнена")
    )
    task_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    task_type = models.CharField(max_length=2, choices=TASK_TYPE_CHOICES)
    status = models.CharField(max_length=11, choices=TASK_STATUS_CHOICES, default=STATUS_CREATED)

    def __str__(self):
        optional_fields = []
        if any([self.name, self.description]):
            optional_fields = [f"[name={self.name}]", f"[description={self.description}]"]

        return f"task_type={self.task_type}, status={self.status}{', '.join(optional_fields)}"

class Result(models.Model):
    result_id = models.OneToOneField(
        Task,
        on_delete = models.CASCADE,
        primary_key=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return f"content={self.content}"
