"""
Main URL configuration for the OrderManagementBackend project.
Defines top-level URL patterns and includes app-specific routes.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

# API routes for project applications
api_patterns = [
    path("users/", include("users.urls")),
    path("products/", include("products.urls")),
    # path("orders/", include("orders.urls")),
    # path("cart/", include("cart.urls")),
]

# Documentation routes for DRF Spectacular
docs_patterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

# Main URL patterns
urlpatterns = [
    # Admin routes
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),  # Honeypot for security
    path("boss/", admin.site.urls),  # Custom admin path
    # API routes
    path("api/", include(api_patterns)),
    path("api/", include("orders.urls")),
    path("api/", include("cart.urls")),
    # Documentation routes
    path("api/", include(docs_patterns)),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
