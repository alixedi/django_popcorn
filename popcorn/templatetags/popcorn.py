from django import template
from django.conf import settings
from django.template.loader import get_template


register = template.Library()

@register.simple_tag(takes_context=True)
def popcorn(context, field):
    field_type = field.field.__class__.__name__
    if field_type in ['ModelChoiceField', 'ModelMultipleChoiceField']:
        model = field.field.queryset.model
        model_name = model._meta.object_name
        app_name = model._meta.app_label
        full_name = "%s.%s" % (app_name, model_name)
        if full_name in settings.POPCORN_MODELS:
            view_name = '%s_%s_popcorn' % (app_name.lower(), 
                                           model_name.lower())
            perm = '%s.add_%s' % (app_name.lower(), 
                                  model_name.lower())
            if perm in context['perms']:
                context['field_name'] = field.name
                context['view_name'] = view_name
                return get_template('popcorn/link.html').render(context)
    return ''