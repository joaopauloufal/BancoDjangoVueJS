from rest_framework import routers
from banco.api import BancoViewSet

router = routers.DefaultRouter()
router.register(r'bancos', BancoViewSet)

urlpatterns = router.urls
