from django.db import models

# Create your models here.
class ArrModel(models.Model):
    length = models.IntegerField(default=5)
    max_val = models.IntegerField(default=100)
    min_val = models.IntegerField(default=1)
    # arr = models.CharField(max_length=1000)

