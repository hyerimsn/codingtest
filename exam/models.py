from django.db import models

# Create your models here.
class Seed(models.Model):
    name = models.TextField(max_length=20)
    age = models.TextField(max_length=20) #여기서 age가 non-nullable 하다는데 잘 모르겠어유,,,,ㅎㅎ,,,
    major = models.TextField(max_length=20)

class Answer(models.Model):
    answer = models.TextField(max_length=100)