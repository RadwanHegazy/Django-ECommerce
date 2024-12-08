from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce APIs",
        default_version='v1',
        description="E-Commerce API documentation",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/',include('dj_auth_package.urls')),
    path('api/v1/category/', include('category.urls')),
    path('api/v1/product/', include('product.urls')),
    path('__docs__/', schema_view.with_ui('swagger', cache_timeout=0), name='docs'),
]
