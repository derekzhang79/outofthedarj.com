import random

from django.shortcuts import render_to_response

from rhythms.models import Rhythm, PracticeMedia
    
def rhythm(request):
    rhythms = Rhythm.objects.all()

    # If rhythm is requested, get it from the database.
    if 'id' in request.GET:
        slug=request.GET['id']
    else: 
        # Otherwise, grab a random rhythm.
        element = random.randrange(0, len(rhythms)) 
        slug=rhythms[element].slug
    
    rhythm = rhythms.filter(slug__iexact=slug)
    
    songs = []
    ry =  [] # ry for grabbing audio
    
    for ry in rhythm:
        songs = ry.song.all()
    
    audio_list = PracticeMedia.objects.filter(rhythm__iexact=rhythm)
    
    return render_to_response('rhythms.html', 
                              {'rhythms': rhythms, 'rhythm': rhythm, 'songs': songs, 'audio_list': audio_list})


