from rest_framework.routers import DefaultRouter
from local_apps.services.views import ServicesViewSet

router = DefaultRouter()
router.register(prefix='services', viewset=ServicesViewSet)

urlpatterns = router.urls