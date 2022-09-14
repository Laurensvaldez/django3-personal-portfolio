from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    text = models.TextField(max_length=250)

    def __str__(self):
        return self.title
