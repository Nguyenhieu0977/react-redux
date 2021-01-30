from rest_framework import routers
from .api import ItViewSet

router = routers.DefaultRouter()
router.register('api/it', ItViewSet, 'it')

urlpatterns = router.urls
