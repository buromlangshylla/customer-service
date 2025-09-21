from rest_framework.routers import SimpleRouter
from .views import (CustomerViewSet, AddressViewSet, KycDocumentViewSet, PaymentMethodViewSet)

router = SimpleRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'kyc-documents', KycDocumentViewSet)
router.register(r'payment-methods', PaymentMethodViewSet)

urlpatterns = router.urls

