from django.contrib.auth.models import AbstractUser
from django.db import models

class advisor(models.Model):
    user = models.ForeignKey('HubUser', on_delete=models.CASCADE, related_name='advisors')

    def __str__(self) -> str:
        return self.user.username

class club(models.Model):
    name = models.CharField(max_length=255,unique=True)
    advisor = models.ForeignKey(advisor, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

class HubUser(AbstractUser):
    department = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=50)
    club = models.ManyToManyField(club)

    def __str__(self) -> str:
        return self.username

class event(models.Model):
    club = models.ForeignKey(club, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,unique=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    
    def __str__(self) -> str:
        return self.name

class feedback(models.Model):
    user = models.ForeignKey(HubUser, on_delete=models.CASCADE)
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"{self.feedback} ({self.event.eventName})"
