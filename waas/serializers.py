from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from django.conf import settings

class BeneficiarySerializer(serializers.Serializer):
    MerchantCode = settings.WAAS_MERCHANT_CODE
    FirstName = serializers.CharField()
    MiddleName = serializers.CharField()
    LastName = serializers.CharField()
    CountryCode = serializers.CharField()
    MobileNumber = serializers.CharField()
    DocumentType = serializers.CharField()
    DocumentNumber= serializers.CharField()
    Email = serializers.EmailField()
