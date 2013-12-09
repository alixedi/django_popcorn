=============================
django_popcorn
=============================

.. image:: https://badge.fury.io/py/django_popcorn.png
    :target: http://badge.fury.io/py/django_popcorn
    
.. image:: https://travis-ci.org/alixedi/django_popcorn.png?branch=master
        :target: https://travis-ci.org/alixedi/django_popcorn

.. image:: https://pypip.in/d/django_popcorn/badge.png
        :target: https://crate.io/packages/django_popcorn?version=latest


Add-another pop-ups a la django-admin. 

The popup views are implemented using a mixin to the generic CreateView. Also, the popups now support permissions. As a result, a user will onle get the 'add-another' link next to a ForeignKey if he has the add permission for the target model.  

Installation
------------

Get it from the cheeseshop: ::

    pip install django_coffee_table


Usage
-----

Read on: 

1. Include the following in your `INSTALLED_APPS` settings: ::

    'popcorn',
    'reform',
    'bootstrap_toolkit',
    'widget_tweaks',

2. Uncomment `django.contrib.admin` in the `INSTALLED_APPS` settings.

3. Add this to your settings.py (If you do not already have it): ::

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.contrib.messages.context_processors.messages",
        "django.core.context_processors.request",
        "popcorn.context_processors.admin_media_prefix",
    )

4. Add the following to your base.html template: ::

    <script src="{{ ADMIN_MEDIA_PREFIX }}js/admin/RelatedObjectLookups.js"></script>

5. Write a few views - use PopcornMixin for popup views: ::

    class CreateUser(CreateView):
        model = User

    class PopcornGroup(PopcornMixin, CreateView):
        model = Group

    class PopcornPermission(PopcornMixin, CreateView):
        model = Permission 

6. Use the utility function to generate popcorn urls: ::

    urlpatterns += get_popcorn_urls([PopcornGroup, PopcornPermission])

7. Render your forms using `django_reform` reform tag: :: 

    {% reform form %}

8. If you are having any problems, please check out the demo project for a working implementation.