from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category = models.TextField()
    def __str__(self) -> str:
        return self.category
    
class Todo(models.Model):
    todo=models.TextField()
    status = models.CharField(max_length=200, blank=True)
    priority = models.CharField(max_length=200, blank=True)
    due_date = models.DateField(blank=True)
    pic = models.CharField(blank=True, max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.todo)
