from django_tenants.utils import tenant_context
from rest_framework.views import APIView
from .models import Sweet
#from serializacion import SweetTypeSerialize
from django.http import JsonResponse
from rest_framework import serializers



class SweetSerialize(serializers.ModelSerializer):
    class Meta:
        model = Sweet
        fields = '__all__'


class SweetList(APIView):
    def get(self, request):
        with tenant_context(request.tenant):
            print(request.tenant)
            print(request)
            sweets = Sweet.objects.all()
            serializer = SweetSerialize(sweets, many=True)
            return JsonResponse(serializer.data, safe=False)
