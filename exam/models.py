from django.db import models

# Create your models here.
class Seed(models.Model):
    name = models.TextField(max_length=20)
    age = models.TextField(max_length=20)
    major = models.TextField(max_length=20)

class Answer(models.Model):
    answer = models.TextField(max_length=100)