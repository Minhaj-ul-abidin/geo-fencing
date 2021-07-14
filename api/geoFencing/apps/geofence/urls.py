from django.urls import path

from .views import ServiceAreaViewSet, ServiceProviderViewSet

urlpatterns = [
    path(
        "providers/",
        ServiceProviderViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="providers-list",
    ),
    path(
        "providers/<uuid:pk>/",
        ServiceProviderViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="providers-detail",
    ),
    path(
        "service-areas/",
        ServiceAreaViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="service-areas-list",
    ),
    path(
        "service-areas/<uuid:pk>/",
        ServiceAreaViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="service-areas-detail",
    ),
]