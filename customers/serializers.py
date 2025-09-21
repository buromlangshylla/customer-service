from rest_framework import serializers
from .models import Customer, Address, KycDocument, PaymentMethod


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ('id',)


class KycDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = KycDocument
        fields = '__all__'
        read_only_fields = ('id', 'uploaded_at', 'verified_at')


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
        read_only_fields = ('id', 'customer', "last_used_at")


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')


class CustomerRetrieveSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)
    kyc_documents = KycDocumentSerializer(many=True, read_only=True)
    payment_methods = PaymentMethodSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = [
            'id', 'first_name', 'last_name', 'dob', 'gender', 'primary_email', 'primary_phone',
            'preferred_contact_method', 'occupation', 'income_bracket', 'risk_score', 'kyc_status',
            'created_at', 'updated_at', 'addresses', 'kyc_documents', 'payment_methods'
        ]
        read_only_fields = ('id', 'created_at', 'updated_at')
