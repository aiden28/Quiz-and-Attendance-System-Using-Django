from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.name