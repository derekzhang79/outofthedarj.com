from django.conf.urls.defaults import *
from django.conf import settings
from views import coming_soon, base_template
from testimonials.views import random_testimonial
from audio_video.views import audio_video
from students.views import classes, about
from events.views import events

# enable admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    #(r'^$', coming_soon),
    (r'^$', random_testimonial),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # URLs for the rhythm pages
    (r'^rhythms/$', include('rhythms.urls')),
    
    (r'^av/$', audio_video),
    
    (r'^classes/$', classes),
    
    (r'^events/$', events),

    (r'^about/$', about),
    
    # FOR TEST SEVER ONLY!!!  Loading static stylesheet for template, only when DEBUG is True
    (r'media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': '/media/storage/code/django/ootd/media'}),
            
    # flatpages - about us, contact us, etc.
    #(r'', include('django.contrib.flatpages.urls')),

)


