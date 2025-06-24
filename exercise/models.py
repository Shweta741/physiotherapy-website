from django.db import models
from django.utils import timezone

class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)  # used for login
    dob = models.DateField()
    gender = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)
    email = models.EmailField()  # removed unique=True
    password = models.CharField(max_length=100)

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    conditions = models.TextField(blank=True, null=True)
    reason = models.CharField(max_length=100, blank=True, null=True)
    previous_sessions = models.CharField(max_length=3, blank=True, null=True)
    appointment = models.TimeField(blank=True, null=True)

    emergency_name = models.CharField(max_length=100)
    emergency_relation = models.CharField(max_length=50)
    emergency_phone = models.CharField(max_length=15)

    insurance = models.CharField(max_length=100, blank=True, null=True)
    policy = models.CharField(max_length=50, blank=True, null=True)
    report = models.FileField(upload_to='reports/', blank=True, null=True)
    newsletter = models.BooleanField(default=False)

    status = models.CharField(
    max_length=10,
    choices=[('Pending', 'Pending'), ('Completed', 'Completed')],
    default='Pending'
)

    def __str__(self):
        return self.full_name

class Feedback(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    submitted_at = models.DateTimeField(default=timezone.now)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.patient.full_name} - {self.rating}★"
    
class ConsultationRequest(models.Model):
    MODE_CHOICES = [
        ('Video', 'Video'),
        ('Call', 'Call')
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptoms = models.TextField()
    preferred_time = models.TimeField()
    mode = models.CharField(max_length=10, choices=MODE_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.full_name} ({self.mode}) - {self.submitted_at.strftime('%Y-%m-%d')}"
