from django.conf import settings


def admin_media_prefix(request):
    '''
    Starting from django 1.4, the static files belonging to django admin follow
    the standard conventions.
    '''
    return {'ADMIN_MEDIA_PREFIX': settings.STATIC_URL + 'admin/' }