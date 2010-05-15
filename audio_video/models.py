from django.db import models

class AudioAndVideo(models.Model):
    
    CATEGORIES = (
        ('Audio', 'Audio'),
        ('Video', 'Video'),
    )
    category = models.CharField(max_length=10, choices=CATEGORIES)
    name = models.CharField(max_length=100)
    link = models.TextField()
    
    class Meta:
        ordering = ['category', 'name']
    
    def __unicode__(self):
        return self.name
    
    
    
    
    