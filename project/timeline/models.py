from django.db import models

class Timeline(models.Model):
    content = models.CharField(max_length=140, verbose_name='content')
    posted_date = models.DateTimeField(auto_now_add=True)