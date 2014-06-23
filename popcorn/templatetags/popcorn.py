from django import template
from django.template.loader import get_template


register = template.Library()

@register.simple_tag(takes_context=True)
def popcorn(context, field):
    model = field.field.queryset.model
    model_name = model._meta.object_name.lower()
    app_name = model._meta.app_label.lower()
    view_name = '%s_%s_popcorn' % (app_name, model_name)
    perm = '%s.add_%s' % (app_name, model_name)
    context['field_name'] = field.name
    context['view_name'] = view_name
    context['has_perm'] = perm in context['perms']
    return get_template('popcorn/link.html').render(context)

@register.filter
def get_form_field_type(field):
    """Returns value for the given field for a form."""
    return field.field.__class__.__name__
