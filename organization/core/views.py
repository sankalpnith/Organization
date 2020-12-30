from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response


class BaseModelViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    model = None
    base_auth_permissions = (
        permissions.IsAuthenticated,
    )
    action_serializers = {}

    http_method_names = ['get', 'post', 'put', 'delete', 'options']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return self.apply_queryset_filters(queryset)

    def apply_queryset_filters(self, queryset):
        return queryset

    def get_serializer_class(self):
        action = self.action.lower()
        if action in self.action_serializers:
            self.serializer_class = self.action_serializers[action]
        return super().get_serializer_class()

    def get_permissions(self):
        permissions_list = self.base_auth_permissions + self.permission_classes
        return [permission() for permission in permissions_list]


class PingAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(data="pong")
