from django.conf import settings
from django.contrib.gis.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from geoFencing.apps.common.models import CoreModel

class ServiceProvider(CoreModel):

    name = models.CharField(verbose_name=_("Service Provider Name"), max_length=150)

    email = models.EmailField(_("Service Provider Email"), max_length=150)

    phone_number = models.CharField(max_length=17)
    language = models.CharField(max_length=50, default=settings.LANGUAGE_CODE)
    currency = models.CharField(max_length=50, default="USD")
    
class ServiceArea(CoreModel):

    service_provider = models.ForeignKey(
        ServiceProvider,
        on_delete=models.CASCADE,
        related_name="service_areas_of",
    )

    name = models.CharField(verbose_name=_("Service Area Name"), max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    service_area = models.PolygonField()
    
    class Meta:
        ordering = ["name"]