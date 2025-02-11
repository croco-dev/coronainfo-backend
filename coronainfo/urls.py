from django.conf.urls import url, include
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers
from patients.views import PatientLocationViewSet, PatientReportViewSet, PatientViewSet
from movements.views import MovementViewSet
from feeds.views import FeedViewSet
from versions.views import VersionViewSet
from reports.views import ReportViewSet
from news.views import NewsViewSet
from notice.views import NoticeViewSet
from crawl.views import CrawlViewSet, LocationCrawlViewSet, TempCrawlViewSet
from cheer.views import CheerViewSet
from .permissions import IsAdminOrReadOnly

ROUTER = routers.DefaultRouter()
ROUTER.register("notice", NoticeViewSet)
ROUTER.register("reports", ReportViewSet, basename={"reports"})
ROUTER.register("reports/patients", PatientReportViewSet, basename={"patient report"})
ROUTER.register("reports/location", PatientLocationViewSet, basename={"location report"})
ROUTER.register("news", NewsViewSet, basename={"news"})
ROUTER.register("crawl", CrawlViewSet, basename={"crawl"})
ROUTER.register("crawl/temp", TempCrawlViewSet, basename={"location"})
ROUTER.register("crawl/location", LocationCrawlViewSet, basename={"temp"})
ROUTER.register("feeds", FeedViewSet)
ROUTER.register("versions", VersionViewSet)
ROUTER.register("patients", PatientViewSet)
ROUTER.register("movements", MovementViewSet)
ROUTER.register("cheer", CheerViewSet)



urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^", include(ROUTER.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
