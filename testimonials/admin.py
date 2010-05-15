from django.contrib import admin
from ootd.testimonials.models import Testimonial

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Testimonial)