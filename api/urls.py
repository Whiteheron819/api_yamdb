from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.users import UserViewSet
from api.views.titles import TitlesViewSet
from api.views.categories import CategoriesViewSet
from api.views.genres import GenresViewSet

router_v1 = DefaultRouter()
router_v1.register("users", UserViewSet, basename="Users")
router_v1.register("titles", TitlesViewSet, basename="Title")
router_v1.register("categories", CategoriesViewSet, basename="Category")
router_v1.register("genres", GenresViewSet, basename="Genre")


urlpatterns = [
    path("v1/", include(router_v1.urls)),
]
