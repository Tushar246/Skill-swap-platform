from django.db import models

# Create your models here.
AVAILABILITY_CHOICES = [
    ("weekends", "Weekends"),
    ("evenings", "Evenings"),
    ("weekdays", "Weekdays"),
]

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)
    rating = models.FloatField(default=0.0)
    public = models.BooleanField(default=True)

class Skill(models.Model):
    name = models.CharField(max_length=50)

class OfferedSkill(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='offered_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

class WantedSkill(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='wanted_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
