from django.conf.urls import url, include
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers
from patients.views import PatientViewSet
from movements.views import MovementViewSet
from feeds.views import FeedViewSet
from versions.views import VersionViewSet
from reports.views import ReportViewSet
from .permissions import IsAdminOrReadOnly

ROUTER = routers.DefaultRouter()
ROUTER.register("patients", PatientViewSet)
ROUTER.register("movements", MovementViewSet)
ROUTER.register("feeds", FeedViewSet)
ROUTER.register("versions", VersionViewSet)
ROUTER.register("reports", ReportViewSet)


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^", include(ROUTER.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
