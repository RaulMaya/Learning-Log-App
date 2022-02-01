from django.db import models

# Create your models here.
# Documentation: https://docs.djangoproject.com/en/2.2/ref/models/fiels/ 

class Topic(models.Model):
    '''This corresponds to the topic that the user is learning about'''
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Returns a string in representation of a model'''
        return self.text