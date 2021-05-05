from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):

    title = models.CharField(max_length=40)
    description =  models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    completedAt = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title