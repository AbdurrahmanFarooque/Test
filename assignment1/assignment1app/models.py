from django.db import models


class User(models.Model):
          name = models.CharField(max_length=255)
          age = models.IntegerField()
          place = models.CharField(max_length=255)
          photo = models.ImageField(null=True, blank=True, upload_to='images/')
          email = models.EmailField()
          password = models.CharField(max_length=12)


class Gallery(models.Model):
        title = models.CharField(max_length=50)
        photo = models.ImageField(upload_to='images/')
        photo_details = models.TextField(max_length=1000)


def __str__(self):
        return self.title