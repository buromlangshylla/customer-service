import uuid
from django.db import models


class Base(models.Model):
    created_by = models.CharField(
        max_length=250, editable=False, null=True, blank=True
    )
    modified_by = models.CharField(
        max_length=250, editable=False, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Customer(Base):
    KYC_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected'),
    ]
    CONTACT_METHOD_CHOICES = [
        ('email', 'Email'),
        ('phone', 'Phone'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    primary_email = models.EmailField(unique=True)
    primary_phone = models.CharField(max_length=20, unique=True)
    preferred_contact_method = models.CharField(max_length=10, choices=CONTACT_METHOD_CHOICES)
    occupation = models.CharField(max_length=100)
    income_bracket = models.CharField(max_length=50)
    risk_score = models.DecimalField(max_digits=5, decimal_places=2)
    kyc_status = models.CharField(max_length=10, choices=KYC_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.primary_email})"


class Address(Base):
    ADDRESS_TYPE_CHOICES = [
        ('permanent', 'Permanent'),
        ('correspondence', 'Correspondence'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, related_name='addresses', on_delete=models.CASCADE)
    type = models.CharField(max_length=15, choices=ADDRESS_TYPE_CHOICES)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type.title()} Address for {self.customer}"


class KycDocument(Base):
    DOC_TYPE_CHOICES = [
        ('passport', 'Passport'),
        ('aadhaar', 'Aadhaar'),
        ('pan', 'PAN'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, related_name='kyc_documents', on_delete=models.CASCADE)
    doc_type = models.CharField(max_length=20, choices=DOC_TYPE_CHOICES)
    storage_key = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    verifier_id = models.UUIDField(null=True, blank=True)

    def __str__(self):
        return f"{self.doc_type.title()} for {self.customer}"


class PaymentMethod(Base):
    TYPE_CHOICES = [
        ('bank', 'Bank'),
        ('card', 'Card'),
        ('upi', 'UPI'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, related_name='payment_methods', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    masked_details = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    last_used_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.type.title()} for {self.customer}"
