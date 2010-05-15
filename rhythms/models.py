from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=250)
    album = models.CharField(max_length=250, blank=True, null=True)
    artist = models.CharField(max_length=250, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['title', 'album']

    def __unicode__(self):
        return self.title


class Rhythm(models.Model):
    name = models.CharField(max_length=100)
    time_signature = models.CharField(max_length=10)
    variation_one = models.CharField(max_length=100)
    variation_two = models.CharField(max_length=50, blank=True, null=True)
    variation_three = models.CharField(max_length=50, blank=True, null=True)
    score_image = models.CharField(max_length=100, blank=True, null=True)
    song = models.ManyToManyField(Song, blank=True, null=True)
    video_example = models.TextField(blank=True, null=True)
    short_description = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, help_text='Suggested value automatically generated from rhythm name. Must be unique.')
 
    class Meta:
        ordering = ['time_signature', 'name']

    def __unicode__(self):
        return self.name

 
class PracticeMedia(models.Model):
    label = models.CharField(max_length=20)
    link = models.CharField(max_length=200)
    rhythm = models.ForeignKey(Rhythm)
    
    class Meta:
        ordering = ['label']

    def __unicode__(self):
        return self.label
