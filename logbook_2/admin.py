from django.contrib import admin
from . import models
# Register your models here.
from logbook_2.models import MeetingDetails
from logbook_2.models import Students
from logbook_2.models import StudDetails
admin.site.register(MeetingDetails)
admin.site.register(StudDetails)
admin.site.register(Students)
