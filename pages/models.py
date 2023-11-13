from django.db import models

# Create your models here.
#models -> database table
#create class for a model
class Post(models.Model):
    #models module has functions for datatype declaration
    #like TextField,Charfield,etc 
    text = models.TextField()

    def __str__(self):
        return "p1"
        
