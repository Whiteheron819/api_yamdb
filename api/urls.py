from django.urls import include, path
from rest_framework.routers import DefaultRouter


from .views import TitlesViewSet, CategoriesViewSet, GenresViewSet

router_v1 = DefaultRouter()
router_v1.register("titles", TitlesViewSet, basename="Titles")
router_v1.register("categories", CategoriesViewSet, basename="Categories")
router_v1.register("genres", GenresViewSet, basename="Genres")


urlpatterns = [
    path("v1/", include(router_v1.urls)),
]