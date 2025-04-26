from channels.auth import AuthMiddlewareStack
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections

class JWTAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        query_string = scope.get("query_string", b"").decode("utf-8")
        token = None

        for param in query_string.split("&"):
            if param.startswith("token="):
                token = param.split("=")[1]
                break

        if token:
            try:
                # Проверяем токен
                UntypedToken(token)
                user = self.get_user_from_token(token)
                scope["user"] = user
            except (AuthenticationFailed, Exception):
                scope["user"] = AnonymousUser()
        else:
            scope["user"] = AnonymousUser()

        close_old_connections()
        return self.inner(scope)

    def get_user_from_token(self, token):
        from rest_framework_simplejwt.authentication import JWTAuthentication
        from django.contrib.auth.models import User

        jwt_auth = JWTAuthentication()
        validated_token = jwt_auth.get_validated_token(token)
        user = jwt_auth.get_user(validated_token)
        return user