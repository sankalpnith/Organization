from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from rest_framework import exceptions
from rest_framework_jwt import authentication as jwt_authentication


class JSONWebTokenAuthentication(jwt_authentication.JSONWebTokenAuthentication):
    """
    Token based authentication using the JSON Web Token standard.
    """

    def authenticate(self, request):
        User = get_user_model()
        try:
            return super().authenticate(request)
        except User.DoesNotExist:
            msg = _('Invalid signature.')
            e = exceptions.AuthenticationFailed(msg)
            raise e
