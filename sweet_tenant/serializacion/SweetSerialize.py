from rest_framework import serializers
from sweet_tenant.models import Sweet

class SweetSerialize(serializers.ModelSerializer):
    class Meta:
        model = Sweet
        fields = '__all__'
