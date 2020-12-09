from django.contrib import admin
from .models import *


admin.site.register(Appointment)
admin.site.register(TakeAppointment)

admin.site.register(Ambulance)
admin.site.register(LabTest)
