from django_tenants.utils import tenant_context
from rest_framework.views import APIView
from .models import SweetType
#from serializacion import SweetTypeSerialize
from django.http import JsonResponse
from rest_framework import serializers



class SweetTypeSerialize(serializers.ModelSerializer):
    class Meta:
        model = SweetType
        fields = '__all__'


class SweetTypeList(APIView):
    def get(self, request):
        with tenant_context(request.tenant):
            print(request.tenant)
            print(request)
            sweets = SweetType.objects.all()
            serializer = SweetTypeSerialize(sweets, many=True)
            return JsonResponse(serializer.data, safe=False)