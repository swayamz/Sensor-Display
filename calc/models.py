from django.db import models
from django.contrib.postgres.fields import JSONField

class FarmData(models.Model):
    time = models.CharField(max_length=50)
    x = models.CharField(max_length=15)
    y = models.CharField(max_length=15)
    value = models.IntegerField()

class FarmDataJSON(models.Model):
    json = JSONField()