import random

from django.shortcuts import render_to_response

from audio_video.models import AudioAndVideo

def audio_video(request):
    av_list = AudioAndVideo.objects.all()
    return render_to_response('av.html', {'av_list': av_list})
    
