from rest_framework import serializers

from .models import ServiceArea, ServiceProvider

class ServiceAreaSerializer(serializers.ModelSerializer):

    provider_name = serializers.SerializerMethodField()

    def get_provider_name(self, obj):
        return str(obj.service_provider)

    class Meta:
        model = ServiceArea
        fields = (
            "uuid",
            "service_provider",
            "provider_name",
            "name",
            "price",
            "service_area",
            "created",
            "updated",
        )
        read_only_fields = ("created", "updated", "provider_name")

class ServiceProviderSerializer(serializers.ModelSerializer):

    # service_areas = serializers.ServiceAreaSerializer()


    class Meta:
        model = ServiceProvider
        fields = (
            "uuid",
            "name",
            "email",
            "phone_number",
            "language",
            "currency",
            "created",
            "updated",
        )
        read_only_fields = ("created", "updated")