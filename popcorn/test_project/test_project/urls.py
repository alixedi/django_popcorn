from django.conf.urls import patterns, url, include
from django.views.generic import CreateView

from popcorn.utils import get_popcorn_urls

from bookstore.models import Book


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 
    	CreateView.as_view(model=Book, success_url='.'), 
    	name='bookstore_book_create'),
    
    url(r'^admin/', include(admin.site.urls)),
)

# We need this to auto-magically create the views and the urls for popups
urlpatterns += get_popcorn_urls()
