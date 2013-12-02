from django.http import HttpResponse
from django.utils.html import escape


class PopcornMixin(object):
    """Cool popups when mixed with FormViews"""
    template_name = 'popcorn/popcorn.html'

    def form_valid(self, form):
        """
        Plug-in the pre_render hook plus the special popup response
        that closes the popup.
        """
        new_obj = form.save()
        return HttpResponse("""
            <script type="text/javascript">
                opener.dismissAddAnotherPopup(window, "%s", "%s");
                $('.selectpicker').selectpicker('render');
            </script>""" % (escape(new_obj._get_pk_val()), escape(new_obj)))