from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.users import UserViewSet

router_v1 = DefaultRouter()
router_v1.register("users", UserViewSet, basename="Users")


urlpatterns = [
    path("v1/", include(router_v1.urls)),
]
