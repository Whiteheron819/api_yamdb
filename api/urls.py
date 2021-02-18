from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (UserViewSet,
                    TitlesViewSet, CategoriesViewSet, GenresViewSet,
                    CommentViewSet, ReviewViewSet)


router_v1 = DefaultRouter()
router_v1.register("users", UserViewSet, basename="users")
router_v1.register("titles", TitlesViewSet, basename="titles")
router_v1.register("categories", CategoriesViewSet, basename="categories")
router_v1.register("genres", GenresViewSet, basename="genres")
router_v1.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewViewSet, basename='reviews'),
router_v1.register(r'titles/(?P<title_id>\d+)/'
                   r'reviews/(?P<review_id>\d+)/comments',
                   CommentViewSet, basename='comments'),

urlpatterns = [
    path("v1/", include(router_v1.urls)),
]
