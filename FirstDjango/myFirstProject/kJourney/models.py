from django.db import models

# Create your models here.
from django.db import models

class LearningJourney(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def str(self):
        return self.title

class AboutMe(models.Model):
    name = models.CharField(max_length=50, default="Kalpana")
    age = models.IntegerField()
    email = models.EmailField()
    bio = models.TextField()

    def str(self):
        return self.name
