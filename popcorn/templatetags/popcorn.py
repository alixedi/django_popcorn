from django import template
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse


register = template.Library()

@register.filter(is_safe=True, needs_autoescape=True)
def get_popup_link(field, autoescape=None):
    """
    Returns link to popups. Used in FormViews to put in + for
    ForeignKey fields. Field here refer to field of forms.
    """
    model = field.field.queryset.model
    model_name = model._meta.object_name.lower()
    app_name = model._meta.app_label.lower()
    view_name = '%s_%s_popcorn' % (app_name, model_name)
    link = ""
    try:
        href = reverse(view_name)
        link = mark_safe("<a href='%s' \
            class='add-another' id='add_id_%s' \
            onclick='return showAddAnotherPopup(this);'> + </a>" \
            % (href, field.name))
    except:
        pass
    return link
