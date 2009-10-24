import random
from django.shortcuts import render_to_response
from ootd.testimonials.models import Testimonial

def random_testimonial(request):
    test_list = Testimonial.objects.all()
    element = random.randrange(0, len(test_list))
    return render_to_response('index.html', {'testimonial': test_list[element]})
