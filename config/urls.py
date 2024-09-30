from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponseRedirect

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from rest_framework.routers import DefaultRouter

from thelastriff.views import GuitarraViewSet, PedidoViewSet, ItemPedidoViewSet


from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

router = DefaultRouter()
router.register(r"guitarras", GuitarraViewSet)
router.register(r"pedidos", PedidoViewSet)
router.register(r"itempedidos", ItemPedidoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(router.urls)), 
    path("api/media/", include(uploader_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path('', lambda request: HttpResponseRedirect('/admin/')),  # Redireciona a URL raiz para a página de administração
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)