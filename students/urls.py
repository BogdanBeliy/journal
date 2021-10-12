from django.conf.urls import url
from django.urls import path
from .views import StudentViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(openapi.Info(
    title='Students API',
    default_version='v1',
    description='Students journal API',
    contact=openapi.Contact(email='uxui.des@gmail.com'),
    license=openapi.License(name='BSD license')
), public=True, permission_classes=(permissions.AllowAny,))


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
    path('students/', StudentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('students/<int:pk>', StudentViewSet.as_view({'get': 'retrieve', 'post': 'update'})),
]
