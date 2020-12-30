from .serializers import ConferenceRoomSerializer
from core.views import BaseModelViewSet

from .models import ConferenceRoom
from . import permissions as room_permissions


class ConferenceRoomViewSet(BaseModelViewSet):

    model = ConferenceRoom
    serializer_class = ConferenceRoomSerializer
    permission_classes = ()

    def get_permissions(self):
        if self.action:
            if self.action.lower() == 'list':
                self.permission_classes += (
                    room_permissions.CanViewRoom,
                )
            elif self.action.lower() == 'create':
                self.permission_classes += (
                    room_permissions.CanCreateRoom,
                )
            elif self.action.lower() == 'partial_update':
                self.permission_classes += (
                    room_permissions.CanEditRoom,
                )
            elif self.action.lower() == 'destroy':
                self.permission_classes += (
                    room_permissions.CanDeleteRoom,
                )
        return super().get_permissions()
