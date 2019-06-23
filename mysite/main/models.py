from django.db import models

# Create your models here.
class ToDoList(models.Model):
	date = models.DateTimeField("date published")
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Item(models.Model):
	text = models.CharField(max_length=500)
	toDoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	complete = models.BooleanField()

	def __str__(self):
		return self.text