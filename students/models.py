from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    blurb = models.TextField()
    bio = models.TextField(null=True, blank=True)
    student_of_the_month = models.BooleanField()
    ootd_member = models.BooleanField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

