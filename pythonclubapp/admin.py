from django.contrib import admin
from .models import MeetingType, Meeting, Review
# Register your models here.
admin.site.register(MeetingType)
admin.site.register(Meeting)
admin.site.register(Review)