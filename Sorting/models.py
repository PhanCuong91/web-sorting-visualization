from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class ArrModel(models.Model):
    length = models.IntegerField(default=5)
    max_val = models.IntegerField(default=100)
    min_val = models.IntegerField(default=1)
    arr = ArrayField(models.IntegerField(), default=[40,6,2,1,10])

