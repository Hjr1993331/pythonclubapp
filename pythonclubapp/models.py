from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class MeetingMinute(models.Model):
    attendance=models.CharField(max_length=255)
    minutestext=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.attendance

    class Meta:
        db_table='meetingminute'

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetinglocation=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    meetingtype=models.ForeignKey(MeetingMinute, on_delete=models.DO_NOTHING)
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
    time=models.TimeField()
    date=models.DateField()
    text=models.TextField()
    url=models.URLField()
    description=models.TextField()                   

    def __str__(self):
        return self.name

    class Meta:
        db_table='resource' 





# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.
# '''
# Models for techreviews:
# Models become tables in the database.
# Each model has an autonumbered id by default, though you can
# change that and delare your own primary keys. 
# I won't do that here.
# TechType, which describes the type of tech product, laptop, tablet, software
# etc. Product--the actual product, 
# We are going to use the django built-in User model to store our users
# Review to store the reviews
# THESE ARE NOT THE MODELS FOR PYTHON CLUB--
# LOOK AT THE ASSIGNMENT
# '''
# class TechType(models.Model):
#     typename=models.CharField(max_length=255)
#     typedescription=models.TextField(null=True, blank=True)

#     def __str__(self):
#         return self.typename
    
#     class Meta:
#         db_table='techtype'

# class Product(models.Model):
#     productname=models.CharField(max_length=255)
#     producttype=models.ForeignKey(TechType, on_delete=models.DO_NOTHING)
#     user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     dateentered=models.DateField()
#     price=models.DecimalField(max_digits=6, decimal_places=2)
#     producturl=models.URLField()
#     description=models.TextField()
        

#     def __str__(self):
#         return self.productname

#     class Meta:
#         db_table='product'

# class Review(models.Model):
#     title=models.CharField(max_length=255)
#     user=models.ForeignKey(User, on_delete=models.CASCADE)
#     product=models.ForeignKey(Product, on_delete=models.CASCADE)
#     reviewdate=models.DateField()
#     reviewtext=models.TextField()

#     def __str__(self):
#         return self.title

#     class Meta:
#         db_table='review'