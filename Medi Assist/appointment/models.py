from django.db import models
from django.urls import reverse
from django.utils import timezone
from accounts.models import User

department = (
    ('Dentistry', "Dentistry"),
    ('Cardiology', "Cardiology"),
    ('ENT Specialists', "ENT Specialists"),
    ('Astrology', 'Astrology'),
    ('Neuroanatomy', 'Neuroanatomy'),
    ('Blood Screening', 'Blood Screening'),
    ('Eye Care', 'Eye Care'),
    ('Physical Therapy', 'Physical Therapy'),
)


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=100)
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    qualification_name = models.CharField(max_length=100)
    institute_name = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)
    department = models.CharField(choices=department, max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name

    # def get_absolute_url(self):
    # return reverse('appointment:delete-appointment', kwargs={'pk': self.pk})


class TakeAppointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    m_phone_number = models.CharField(max_length=120)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name


class Ambulance(models.Model):
    title = models.CharField(max_length=120)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class LabTest(models.Model):
    name = models.CharField(max_length=50)
    fee = models.IntegerField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name
