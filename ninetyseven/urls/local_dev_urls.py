from django.conf.urls.defaults import *
from django.views.static import serve
from django.conf import settings

urlpatterns = patterns('',
  # STATIC files
  url(
    regex   = r'^archetype/(?P<path>.*)$',
    view    = serve,
    name    = 'serve',
    kwargs  = { 'document_root': settings.STATIC_ROOT, 'show_indexes': True, }
  ),
  # MEDIA files (user uploads)
  url(
    regex   = r'^ninetyseven/(?P<path>.*)$',
    view    = serve,
    name    = 'serve',
    kwargs  = { 'document_root': settings.MEDIA_ROOT, 'show_indexes': True, }
  ),
)
