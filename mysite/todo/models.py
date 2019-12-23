from django.db import models

# Create your models here.

class Todo_List(models.Model):
    task = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.task