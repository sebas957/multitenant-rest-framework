from django.db import models
from django_tenants.models import TenantMixin

from sweet_shared.models import SweetType

class Sweet(TenantMixin, models.Model):
    sweet_type = models.ForeignKey(SweetType, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
