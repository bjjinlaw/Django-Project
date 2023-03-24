from django.db import models
from django.conf import settings

# Create your models here.

class Story(models.Model):
    your_name = models.CharField(max_length=255)
    partner_name = models.CharField(max_length=255)
    your_email = models.CharField(max_length=255)
    partner_email = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="story")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)