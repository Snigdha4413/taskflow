from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE) #handling the case when user is deleted, we want to delete all the tasks of that user
    title = models.CharField(max_length=200)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default="medium")
    due_date = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) #the date and time when the task is created, it will be set automatically when the task is created
    #ask the .something commands in the exams for not predictable fields, so we will use auto_now_add for created_at and auto_now for updated_at

    def __str__(self):
        return self.title