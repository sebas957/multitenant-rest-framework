from django_tenants.utils import tenant_context
from rest_framework.views import APIView
from .models import SweetType
from sweet_shared.serializacion.SweetTypeSerialize import SweetTypeSerialize
from django.http import JsonResponse
from rest_framework import serializers

class SweetTypeList(APIView):
    def get(self, request):
        with tenant_context(request.tenant):
            sweets = SweetType.objects.all()
            serializer = SweetTypeSerialize(sweets, many=True)
            return JsonResponse(serializer.data, safe=False)
