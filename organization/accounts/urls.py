from django.conf.urls import url
from rest_framework_jwt import views as jwt_views
from .import views as accounts_views

urlpatterns = [
    url(
        r'^login/$',
        jwt_views.ObtainJSONWebTokenView.as_view(),
        name='login',
    ),
    url(
        r'^logout/$',
        accounts_views.LogoutViewSet.as_view({
            'delete': 'destroy',
        }),
        name='logout',
    ),
    url(
        r'^roles/$',
        accounts_views.RoleViewSet.as_view({
            'get': 'list',
        }),
        name='roles',
    ),
    url(
        r'^employees/$',
        accounts_views.EmployeeViewSet.as_view({
            'post': 'create',
            'get': 'list',
        }),
        name='employee-create-list',
    ),
    url(
        r'^employees/(?P<pk>[a-f0-9-]+)/$',
        accounts_views.EmployeeViewSet.as_view({
            'put': 'partial_update',
            'delete': 'destroy',
        }),
        name='employee-update-delete',
    ),
]