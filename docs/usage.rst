========
Usage
========

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
