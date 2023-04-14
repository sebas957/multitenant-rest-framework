from django.db import models
from django_tenants.models import TenantMixin

class SweetType(TenantMixin):
    name = models.CharField(max_length=128)
    schema_name = models.CharField(max_length=100, default='demo')

