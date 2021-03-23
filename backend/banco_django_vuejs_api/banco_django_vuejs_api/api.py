from rest_framework import routers
from banco.api import BancoViewSet, AgenciaViewSet, ClienteViewSet

router = routers.DefaultRouter()
router.register(r'bancos', BancoViewSet)
router.register(r'agencias', AgenciaViewSet)
router.register(r'clientes', ClienteViewSet)

urlpatterns = router.urls
