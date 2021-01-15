from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class MeetingMinute(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='meetingminute'

class Meeting(models.Model):
    meetingname=models.CharField(max_length=255)
    productlocation=models.CharField(max_length=255)
    meetingtype=models.ForeignKey(MeetingMinute, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    producttime=models.TimeField()
    dateentered=models.DateField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    meetingurl=models.URLField()
    description=models.TextField()

    def __str__(self):
        return self.meetingname

    class Meta:
        db_table='meeting'

class Resource(models.Model):
    title=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    meeting=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    resourcetime=models.TimeField()
    resourcedate=models.DateField()
    resourcetext=models.TextField()                    

    def __str__(self):
        return self.title

    class Meta:
        db_table='resource' 