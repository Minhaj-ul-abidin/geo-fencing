from django.test import TestCase

# Create your tests here.
import datetime

from django.contrib.gis.geos import Polygon
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import ServiceArea


class ServiceAreaTests(APITestCase):
    def setUp(self):
        "Initial setup"
        self.provier_data = {
            "name": "Alex",
            "email": "alex@gmail.com",
            "phone_number": "+919655782265",
            "language": "En",
            "currency": "USD",
        }
        self.provider = ServiceProvider.objects.create(**self.provier_data)
        self.provider.save()
        self.provider_id = self.provider.uuid
        self.area_polygon = Polygon(
            (
                (14.575939178466795, 25.32432169073797),
                (14.563064575195312, 25.31718389496166),
                (14.573020935058594, 25.289870184457822),
                (14.599456787109373, 25.295147176413156),
                (14.601001739501951, 25.31501143883031),
                (14.575939178466795, 25.32432169073797),
            )
        )
        self.sa_datata = {
            "name": "Test Area",
            "price": "200.00",
            "service_area": self.area_polygon,
        }

        self.sa = ServiceArea.objects.create(
            service_provider=self.provider, **self.sa_datata
        )

        self.sa_id = f"{self.sa.uuid}"
        self.sa_datata["uuid"] = self.sa_id
        self.sa_datata["service_area"] = str(self.sa.service_area)
        self.sa_datata["service_provider"] = self.provider_id
        self.sa_datata["provider_name"] = self.provider.name

        self.new_sa_data = {
            "service_provider": self.provider_id,
            "name": "Test Area 2",
            "price": "200.00",
            "service_area": str(self.area_polygon),
        }

        self.patch_attribute = "price"
        self.area_patch_data = {self.patch_attribute: "300.00"}

    def test_get_service_area_list(self, *args):
        """
        Test GET the service area list.
        """
        url = reverse("service-areas-list")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        api_response = resp.json()
        assert len(api_response) > 0

    def test_get_lat_long_area(self, *args):
        """
        Test GET the service areas containing longitude and latitude.
        """
        url = reverse("service-areas-list")
        resp = self.client.get(url, {"latitude": "15.12321", "longitude": "14.12421"})

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        api_response = resp.json()
        assert len(api_response) == 1

    def test_create_service_area(self):
        """
        Test the POST api on service-area.
        """
        url = reverse("service-areas-list")
        resp = self.client.post(url, self.new_sa_data, format="json")

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        api_response = resp.json()

        assert api_response["name"] == self.new_sa_data["name"]

    def test_get_service_area_detail(self):
        """
        Test the GET detail api on service-area.
        """
        url = reverse("service-areas-detail", kwargs={"pk": self.sa_id})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        api_response = resp.json()
        assert api_response["uuid"] == self.sa_id

    def test_update_service_area(self):
        """
        Test the UPDATE api on service-area.
        """
        url = reverse("service-areas-detail", kwargs={"pk": self.sa_id})
        resp = self.client.patch(
            url,
            data=self.area_patch_data,
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(
            self.area_patch_data[self.patch_attribute],
            resp.json()[self.patch_attribute],
        )

    def test_delete_service_area(self):
        """
        Test the DELETE api on service-area.
        """
        url = reverse("service-areas-detail", kwargs={"pk": self.sa_id})
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ServiceArea.objects.filter(uuid=self.sa_id).exists())