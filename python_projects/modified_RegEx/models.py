from django.db import models

# Create your models here.
class textFile(models.Model):
    content = models.TextField()