from collections import UserString
from genericpath import exists
from pickle import FALSE
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from utils.authentication import get_access_token
from . serializers import (BeneficiarySerializer)
from .models import (DocumentType, WaasAccount,
                     TransactionStaging, TransactionNotification,
                     PaymentDetail, PaymentType,
                     WaasAccountTransaction)
from authentication.models import (Role, User, VerificationCode,
                                    Role)

# Create your views here.


class TestAuthAPIView(APIView):
    def get(self, request):
        token = get_access_token()
        return Response({
            'token': token
        })


class RegisterBeneficiaryAPIView(APIView):
    serializer_class = BeneficiarySerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            MerchantCode = request.data.get('MerchantCode')
            FirstName = request.data.get('firstName')
            MiddleName = request.data.get('MiddleName')
            LastName = request.data.get('LastName')
            CountryCode = request.data.get('CountryCode')
            MobileNumber = request.data.get('MobileNumber')
            DocumentType = request.data.get('DocumentType')
            DocumentNumber = request.data.get('DocumentNumber')
            Email = request.data.get('Email')

            user = User.objects.filter(username=MobileNumber)
            if  User.exists():
                return Response({
                    'status': False,
                    'message': 'User already exists'
                })
        
            access_token = get_access_token()

            return Response({
                'status': True,
                'message': 'Access token',
                'token': access_token})
        return Response(serializer.errors)
