from django.conf import settings
from rest_framework.exceptions import NotAuthenticated
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    if settings.ENABLE_UNAUTHENTICATED_RESULTS \
            and isinstance(exc, NotAuthenticated) \
            and 'view' in context \
            and hasattr(context['view'], "list"):
        return context['view'].list(context['request'])
    return exception_handler(exc, context)
