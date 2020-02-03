from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from patients.views import PatientViewSet
from movements.views import MovementViewSet

router = routers.DefaultRouter()
router.register("patients", PatientViewSet)
router.register("patients", MovementViewSet)

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^", include(router.urls)),
]
