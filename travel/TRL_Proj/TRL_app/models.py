from unicodedata import name
from django.db import models

class place(models.Model):
    name = models.CharField(max_length = 250)
    photo = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    
    # to show only names of photo in the list in admin pannel add this commant
    def __str__(self): 
        return self.name

class team(models.Model):
    name = models.CharField(max_length = 250)
    photo = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
