from django.contrib import admin
from ootd.events.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'name')
    ordering = ('date',)
 
admin.site.register(Event, EventAdmin)
