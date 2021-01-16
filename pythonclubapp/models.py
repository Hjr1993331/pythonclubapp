from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class MeetingMinute(models.Model):
    minutesid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    attendance=models.CharField(max_length=255)
    minutestext=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='meetingminute'

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetinglocation=models.CharField(max_length=255)
    meetingtype=models.ForeignKey(MeetingMinute, on_delete=models.DO_NOTHING)
    meetingid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    meetingtime=models.TimeField()
    dateentered=models.DateField()

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='meeting'

class Resource(models.Model):
    name=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    meeting=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    resourcetime=models.TimeField()
    resourcedate=models.DateField()
    resourcetext=models.TextField()
    resourceurl=models.URLField()
    description=models.TextField()                   

    def __str__(self):
        return self.name

    class Meta:
        db_table='resource' 