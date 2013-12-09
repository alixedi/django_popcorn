from django.conf.urls import patterns, url, include
from django.contrib.auth.models import User, Group, Permission
from django.views.generic import CreateView

from popcorn.viewmixins import PopcornMixin
from popcorn.utils import get_popcorn_urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

class CreateUser(CreateView):
    model = User

class PopcornGroup(PopcornMixin,
                   CreateView):
    model = Group

class PopcornPermission(PopcornMixin,
                        CreateView):
    model = Permission

urlpatterns = patterns('',
    # Examples:
    url(r'^$', CreateUser.as_view(), name='auth_user_create'),
    # url(r'^demo_project/', include('demo_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += get_popcorn_urls([PopcornGroup, PopcornPermission])