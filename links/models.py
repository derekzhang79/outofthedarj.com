from django.db import models

class Link(models.Model):
    name = models.CharField(max_length=120)
    url = models.URLField()

    class Meta:
        ordering = ['name',]

    def __unicode__(self):
        return self.name
    