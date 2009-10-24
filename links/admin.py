from django.contrib import admin
from ootd.links.models import Link

class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    ordering = ('name',)

admin.site.register(Link, LinkAdmin)
