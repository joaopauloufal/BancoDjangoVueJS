from rest_framework import routers
from banco.api import BancoViewSet, AgenciaViewSet

router = routers.DefaultRouter()
router.register(r'bancos', BancoViewSet)
router.register(r'agencias', AgenciaViewSet)

urlpatterns = router.urls
