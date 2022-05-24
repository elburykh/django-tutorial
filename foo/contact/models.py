from django.db import models

class Message(models.Model):
    author = models.TextField()
    content = models.TextField()
