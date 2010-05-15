from django.contrib import admin
from ootd.rhythms.models import Song, PracticeMedia, Rhythm

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')

class PracticeMediaAdmin(admin.ModelAdmin):
    list_display = ('rhythm', 'label')

class RhythmAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_signature', 'short_description')
    list_filter = ('time_signature',)
    ordering = ('time_signature', 'name')
    prepopulated_fields = {'slug': ('name'.replace(' ','-'),)}

admin.site.register(PracticeMedia, PracticeMediaAdmin)
admin.site.register(Rhythm, RhythmAdmin)
admin.site.register(Song, SongAdmin)
