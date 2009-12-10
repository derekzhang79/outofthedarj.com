from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateTimeField()
    blurb = models.CharField(max_length=240)
    location = models.CharField(max_length=200)
    advertisement_image = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    
    class Meta:
        ordering = ['date',]
        
    def __unicode__(self):
        return self.name
    
    
