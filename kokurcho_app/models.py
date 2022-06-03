from django.db import models


class Comment(models.Model):
    email = models.CharField(max_length=50)
    contents = models.TextField()

