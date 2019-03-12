from django.db import models

# Create your models here.
class Newdata(models.Model):
    Task=models.TextField(max_length=100)

    def __str__(self):
        return self.Task
