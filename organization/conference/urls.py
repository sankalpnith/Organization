from django.conf.urls import url
from . import views as conference_views


urlpatterns = [
url(
    r'^rooms/$',
    conference_views.ConferenceRoomViewSet.as_view({
            'post': 'create',
            'get': 'list',
        }),
    name='conference-create-list',
),
url(
    r'^rooms/(?P<pk>[a-f0-9-]+)/$',
    conference_views.ConferenceRoomViewSet.as_view({
            'put': 'partial_update',
            'delete': 'destroy',
        }),
    name='conference-update-delete',
),
    ]