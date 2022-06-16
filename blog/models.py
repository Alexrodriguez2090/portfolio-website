from django.db import models
from datetime import datetime

class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now, blank=True)
    #author = ADDUSER

    body = models.CharField(max_length=5000)


    class Meta:
        app_label = 'blog'

    def __str__(self):
        return f"{self.title}"