from rest_framework import serializers as rf_serializers
from rest_framework import status
from accounts.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



class Tokens(APIView):
    """
    View to Create, Get, and Remove tokens. These tokens
    differ from the JWT Tokens used for user authentication in that
    they never change. These should only be used to allow applications
    access to the API.
    """
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        """
        Creates and returns a new auth token for the authenticated user.
        """
        ret_status = status.HTTP_200_OK
        content = {}
        if 'name' in request.data and len(request.data['name']):
            name = request.data['name']
            token = Token.objects.create(user=request.user, name=name)
            content = {
                'name': name,
                'token': token.key,
            }
        else:
            content = {
                'name': 'This is a required field.'
            }
            ret_status = status.HTTP_400_BAD_REQUEST
        return Response(content, status=ret_status)

    def get(self, request):
        """
        Returns all the tokens for the current user.
        """
        tokens = Token.objects.filter(user=request.user)
        content = [token.key for token in tokens]
        return Response(content)

    def delete(self, request, token):
        Token.objects.filter(key=token).delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
