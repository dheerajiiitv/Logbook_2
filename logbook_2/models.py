from django.db import models
from django.utils import timezone
# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)

class MeetingDetails(models.Model):
    date = models.DateField(primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    today_objective = models.TextField()

class StudDetails(models.Model):
    name = models.ForeignKey(Students,on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(False)
    objective= models.TextField()
