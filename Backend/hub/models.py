from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class club(models.Model):
    clubName = models.CharField(max_length=255,unique=True)
    clubAdvisor = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.clubName
# --------------------------------------------------------------------------------

class user(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    gender = models.CharField(max_length=255)
    club = models.ManyToManyField(club)
    age = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.user.username
    
# --------------------------------------------------------------------------------

class event(models.Model):
    eventClub = models.ForeignKey(club, on_delete=models.CASCADE)
    eventName = models.CharField(max_length=255,unique=True)
    eventDate = models.DateField(null=True)
    eventTime = models.TimeField(null=True)
    
    def __str__(self) -> str:
        return self.eventName
    
# --------------------------------------------------------------------------------

class feedback(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"{self.feedback} ({self.event.eventName})"

# --------------------------------------------------------------------------------