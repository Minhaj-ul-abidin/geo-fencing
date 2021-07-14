import datetime
import logging

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .filters import ServiceAreaFilter
from .models import ServiceArea, ServiceProvider
from .serializers import (ServiceAreaSerializer, ServiceProviderSerializer)

logger = logging.getLogger(__name__)


class ServiceProviderViewSet(viewsets.ModelViewSet):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        logger.info(
            f"User {request.user} GET service-provider-list with args {dict(request.query_params)}"
        )
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        logger.info(
            f"User {request.user} POST service-provider-list with args "
            f"{dict(request.query_params)} and data {request.data}"
        )
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, pk, *args, **kwargs):
        logger.info(
            f"User {request.user} GET service-provider-detail for service-provider"
            f" {pk} with args {dict(request.query_params)}"
        )
        return super().retrieve(request, pk, *args, **kwargs)

    def partial_update(self, request, pk, *args, **kwargs):
        logger.info(
            f"User {request.user} PATCH service-provider-detail for service-provider {pk} with args "
            f"{dict(request.query_params)} and data {request.data}"
        )
        return super().partial_update(request, pk, *args, **kwargs)

    def destroy(self, request, pk, *args, **kwargs):
        logger.info(
            f"User {request.user} DELETE service-provider-detail for service-provider {pk}"
        )
        return super().destroy(request, pk, *args, **kwargs)


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all().prefetch_related('service_provider')
    serializer_class = ServiceAreaSerializer
    permission_classes = [AllowAny]
    filterset_class = ServiceAreaFilter

    def list(self, request, *args, **kwargs):
        logger.info(
            f"User {request.user} GET service-area-list with args {dict(request.query_params)}"
        )
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        logger.info(
            f"User {request.user} POST service-area-list with args "
            f"{dict(request.query_params)} and data {request.data}"
        )
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, pk, *args, **kwargs):
        logger.info(
            f"User {request.user} GET service-area-detail for service-area {pk}"
            f" with args {dict(request.query_params)}"
        )
        return super().retrieve(request, pk, *args, **kwargs)

    def partial_update(self, request, pk, *args, **kwargs):
        logger.info(
            f"User {request.user} PATCH service-area-detail for service-area {pk} with args "
            f"{dict(request.query_params)} and data {request.data}"
        )
        return super().partial_update(request, pk, *args, **kwargs)

    def destroy(self, request, pk, *args, **kwargs):
        logger.info(
            f"User {request.user} DELETE service-area-detail for service-area {pk}"
        )
        return super().destroy(request, pk, *args, **kwargs)
