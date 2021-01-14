from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TechType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='meetingtype'

class Product(models.Model):
    meetingname=models.CharField(max_length=255)
    meetingtitle=models.CharField(max_length=255)
    meetinglocation=models.CharField(max_length=255)
    meetingtype=models.ForeignKey(TechType, on_delete=models.DO_NOTHING)
    meetingid=models.ForeignKey(Id, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateentered=models.DateField()
    meetingurl=models.URLField()
    description=models.TextField()

    def __str__(self):
        return self.meetingname

    class Meta:
        db_table='meeting'

class Review(models.Model):
    title=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    meeting=models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewdate=models.DateField()
    reviewtext=models.TextField()                    

    def __str__(self):
        return self.title

    class Meta:
        db_table='review' 