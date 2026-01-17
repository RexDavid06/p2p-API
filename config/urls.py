"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path
from rest_framework.permissions import AllowAny
from django.views.generic import RedirectView



schema_view = get_schema_view(
    openapi.Info(
        title='PeerToPeer Payment API',
        default_version='v1',
        description='API Documentation',
        contact=openapi.Contact(email='rhexmilia06@gmail.com'),

    ), public=True,
    permission_classes= [AllowAny]
)

urlpatterns = [
    path('', RedirectView.as_view(url='/docs/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/notifications/', include('notifications.urls')),
    path('api/v1/transactions/', include('transactions.urls')),
    path('api/v1/wallets/', include('wallets.urls')),
    #swagger URLS
    re_path(r'^Swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
