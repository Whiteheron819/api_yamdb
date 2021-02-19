from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, TitleViewSet, CategoryViewSet, GenreViewSet, CommentViewSet, ReviewViewSet


router_v1 = DefaultRouter()
router_v1.register("users", UserViewSet, basename="user")
router_v1.register("titles", TitleViewSet, basename="Title")
router_v1.register("categories", CategoryViewSet, basename="Category")
router_v1.register("genres", GenreViewSet, basename="Genre")
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path("v1/", include(router_v1.urls)),
]
