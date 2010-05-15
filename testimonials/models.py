from django.db import models

class Testimonial(models.Model):
    testimonial = models.TextField()
    name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

    # Need to add testimonials to installed apps


