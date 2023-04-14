from django_tenants.utils import tenant_context
from rest_framework.views import APIView
from sweet_tenant.models import Sweet
from sweet_tenant.serializacion.SweetSerialize import SweetSerialize
from django.http import JsonResponse


class SweetList(APIView):
    def get(self, request):
        with tenant_context(request.tenant):
            print(request.tenant)
            print(request)
            sweets = Sweet.objects.all()
            serializer = SweetSerialize(sweets, many=True)
            return JsonResponse(serializer.data, safe=False)
