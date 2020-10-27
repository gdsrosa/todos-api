from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=200)
    done = models.BooleanField()
