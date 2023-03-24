from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


class User(AbstractUser):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class Gender(models.TextChoices):
    MALE = ("male", "MALE")
    FEMALE = ("female", "FEMALE")
    OTHER = ("other", "OTHER")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255, choices=Gender.choices, default=Gender.OTHER)
    contact = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(null=True)
    avatar = models.ImageField(upload_to="Profile", blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    height = models.DecimalField(max_digits=50, decimal_places=1, blank=True, null=True)
    marital_status = models.CharField(max_length=255, blank=True, null=True)
    religion = models.CharField(max_length=255, blank=True, null=True)
    mother_tongue = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True) 
    bio = models.TextField(blank=True, null=True)
    hubby = models.CharField(max_length=255, blank=True, null=True)
    favourite_foods = models.CharField(max_length=255, blank=True, null=True)
    favourite_places = models.CharField(max_length=255, blank=True, null=True)
    

    def __str__(self):
        return str(self.user)

class Education(models.Model):
    college_name = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    percentage = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="educations", blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Job(models.Model):
    company_name = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="jobs", blank=True, null=True)

    def __str__(self):
        return str(self.id)