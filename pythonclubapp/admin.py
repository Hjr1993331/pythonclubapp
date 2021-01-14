from django.contrib import admin
from .models import MeetingType, Meetings, Review
# Register your models here.
admin.site.register(MeetingType)
admin.site.register(Meetings)
admin.site.register(Review)

