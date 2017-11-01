from django.conf import settings
from rest_framework.exceptions import NotAuthenticated
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # if its a view with a list and request attr
    if 'view' in context and hasattr(context['view'], 'list') and hasattr(context['view'], 'request'):
        view = context['view']
        request = view.request

        if request.method == 'GET' and settings.ENABLE_UNAUTHENTICATED_RESULTS and isinstance(exc, NotAuthenticated):
            return view.list(context['request'])

    return exception_handler(exc, context)
