from datetime import datetime

from django.shortcuts import render_to_response

from ootd.events.models import Event

def events(request):
    events = Event.objects.all()
    events_list = events.filter(date__gte=datetime.now())
    event_details = []
    current_event = []
    if 'id' in request.GET:
        event_details = events.filter(id__iexact=request.GET['id'])
    else:
        current_event = events_list[0]
    return render_to_response('events.html',{'events_list': events_list,
                                              'event_details': event_details,
                                              'current_event': current_event})
