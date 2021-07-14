
from django.contrib.gis.geos import Point
from django.urls import reverse
from django_filters import rest_framework as filters

from .models import ServiceArea


class ServiceAreaFilter(filters.FilterSet):
    latitude = filters.NumberFilter(
        max_digits=25,
        method="filter_latitude",
    )
    longitude = filters.NumberFilter(
        max_digits=25,
        method="filter_longitude",
    )

    class Meta:
        model = ServiceArea
        fields = ["latitude", "longitude"]

    def __init__(self, data=None, *args, **kwargs):
        is_list_url = kwargs.get("id") is None and kwargs.get(
            "request"
        ).path == reverse("service-areas-list")
        super().__init__(data, *args, **kwargs)

    def filter_latitude(self, queryset, name, value):
        self.latitude = value
        return queryset

    def filter_longitude(self, queryset, name, value):
        self.longitude = value
        point = Point(float(self.latitude), float(self.longitude))
        queryset = queryset.filter(service_area__contains=point)
        return queryset