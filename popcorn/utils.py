from django.conf import settings
from django.conf.urls import url, patterns
from django.db.models.loading import get_model
from django.views.generic import CreateView
from .viewmixins import PopcornMixin


def get_popcorn_name(model):
    """Get reverse friendly name for this view"""
    app = model._meta.app_label.lower()
    model = model._meta.object_name.lower()
    return "%s_%s_popcorn" % (app, model)


def get_popcorn_view(model):
    """Returns the PopupView for the given model"""
    return type("Popcorn%s" % model._meta.object_name,
                (PopcornMixin, CreateView),
                {'model': model})


def get_popcorn_urls():
    """Returns complete urls if you so like"""
    urls = patterns('')
    for popcorn in settings.POPCORN_MODELS:
        app_label, model_name = popcorn.split(".")
        model = get_model(app_label, model_name)
        urls += patterns('', url(r'^popcorn/%s' % model_name,
                             get_popcorn_view(model).as_view(),
                             name=get_popcorn_name(model)))
    return urls
