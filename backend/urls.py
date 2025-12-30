from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet, weather_api, dashboard

router = DefaultRouter()
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/weather/", weather_api),
    path("dashboard/", dashboard),
]
