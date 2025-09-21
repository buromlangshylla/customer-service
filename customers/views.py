from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny

from .models import Customer, Address, KycDocument, PaymentMethod
from .serializers import (
    CustomerListSerializer,
    CustomerRetrieveSerializer,
    AddressSerializer,
    KycDocumentSerializer,
    PaymentMethodSerializer
)
from .permissions import IsJWTAuthenticated


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['kyc_status', 'income_bracket', 'risk_score']
    search_fields = ['primary_email']

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsJWTAuthenticated()]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CustomerRetrieveSerializer
        return CustomerListSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsJWTAuthenticated()]


class KycDocumentViewSet(viewsets.ModelViewSet):
    queryset = KycDocument.objects.all()
    serializer_class = KycDocumentSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsJWTAuthenticated()]


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsJWTAuthenticated()]
