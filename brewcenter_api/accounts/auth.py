import rest_framework.authentication

from accounts.models import Token


class TokenAuthentication(rest_framework.authentication.TokenAuthentication):
    """
    Extends the DRF TokenAuthentication to use the subclassed Token Model
    defined in this module. This enables users to have multiple tokens.
    """

    model = Token
