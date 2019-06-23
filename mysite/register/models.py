from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import ToDoList

# Create your models here.
class CustomUser(AbstractUser):
	toDoLists = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
