from distutils.command.upload import upload
from django.db import models


class Contact(models.Model):
    name=models.CharField(null=True,max_length=25)
    email=models.EmailField(null=True)
    subject=models.CharField(null=True,max_length=100)
    message=models.TextField(null=True,max_length=800)

    def __str__(self):
        return self.email
