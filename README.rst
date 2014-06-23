=============================
django_popcorn
=============================

.. image:: https://badge.fury.io/py/django_popcorn.png
    :target: http://badge.fury.io/py/django_popcorn
    
.. image:: https://travis-ci.org/alixedi/django_popcorn.png?branch=master
        :target: https://travis-ci.org/alixedi/django_popcorn

.. image:: https://pypip.in/d/django_popcorn/badge.png
        :target: https://crate.io/packages/django_popcorn?version=latest

.. image:: https://coveralls.io/repos/alixedi/django_popcorn/badge.png
  :target: https://coveralls.io/r/alixedi/django_popcorn

Add-another pop-ups a la ``django-admin``. 

The popup views are implemented using a mixin to the generic CreateView. Also, the popups now support permissions. As a result, a user will only get the ``add-another`` link next to a ForeignKey or a ManyToMany field if he has the add permission for the target model. 

Installation
------------

Get it from the cheeseshop: ::

    pip install django_popcorn


Usage
-----

Read on: 

1. Include the following in your ``INSTALLED_APPS`` settings: ::

    'popcorn',

2. Add this to your ``settings.py`` (If you do not already have it): ::

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

    POPCORN_MODELS = ('auth.Group', 'auth.Permission')

3. Add the following to your ``base.html`` template: ::

    <script src="{{ ADMIN_MEDIA_PREFIX }}js/admin/RelatedObjectLookups.js"></script>

4. We will create a view for ``auth.User`` and use the utility ``get_popcorn_urls`` function to generate popcorn views and urls: ::

    urlpatterns = patterns('',
        url(r'^$', CreateView.as_view(model=User, success_url='.'), name='auth_user_create'),
        url(r'^admin/', include(admin.site.urls)),
    )

    urlpatterns += get_popcorn_urls()

7. Render your forms like so: :: 

        <form method="POST" action="{{ request.get_full_path }}">
            {% csrf_token %}
            {% include 'popcorn/form.html' %}
            <button type="submit">Submit</button>
            <a href="../">Cancel</a>
        </form>

Thats it! sync your DB, run the dev server and fire up your browser at localhost. You should see a form **wthout** the ``add-another`` links. This is because popcorn add-another links are only enabled for users who have add permission for the target model. Now log-in - possibly via admin after enabling it and hit localhost again. You should see a little ``+`` next to ForeignKey and ManyToMany fields. Click it and the add-another popup would appear. If you are having any problems, please check out the test project for a working implementation.
