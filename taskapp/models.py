from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Task(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=255)
    description = models.TextField()
    date_created= models.DateTimeField(auto_now_add=True)  
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['completed',]    


        
