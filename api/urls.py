from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import TitlesViewSet, CategoriesViewSet, GenresViewSet

router = DefaultRouter()
router.register("titles", TitlesViewSet, basename="Titles")
router.register("categories", CategoriesViewSet, basename="Categories")
router.register("genres", GenresViewSet, basename="Genres")


urlpatterns = [
    path("v1/", include(router.urls)),
]