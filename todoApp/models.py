from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    deadline = models.DateTimeField('Deadline')
    status = models.BooleanField(default=False)
    priority = models.IntegerField()
    userId = models.IntegerField(default=-1)

    def __str__(self):
        return self.name
