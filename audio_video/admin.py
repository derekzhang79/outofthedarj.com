from django.contrib import admin
from ootd.audio_video.models import AudioAndVideo

class AudioAndVideoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(AudioAndVideo)