from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, generics
from rest_framework.permissions import (IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.viewsets import ModelViewSet

from .models import Categories, Comment, Genres, Review, Titles, User
from .permissions import IsOwnerOrReadOnly
from .serializers import (CategoriesSerializer, CommentSerializer,
                          GenresSerializer, ReviewSerializer, TitlesSerializer,
                          UserSerializer)


class CategoriesViewSet(ModelViewSet):
    permission_classes = [
        IsOwnerOrReadOnly]
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    # filterset_fields = ["slug", "genre__slug", "year", "name"]
    filter_backends = [filters.SearchFilter]
    search_fields = ("name")


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          ]

    def perform_create(self, serializer):
        title = get_object_or_404(Titles, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)

    def get_queryset(self):
        title = get_object_or_404(Titles, pk=self.kwargs.get('title_id'))
        return title.comments.all()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'username'


class TitlesViewSet(ModelViewSet):
    permission_classes = [
        IsOwnerOrReadOnly]
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["slug"]


class MyMixin(generics.CreateAPIView,
              generics.DestroyAPIView,
              generics.ListAPIView,
              viewsets.GenericViewSet):
    ...


class GenresViewSet(MyMixin):
    permission_classes = [IsAuthenticatedOrReadOnly
                          ]
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    # filterset_fields = ["name"]
    filter_backends = [filters.SearchFilter]
    search_fields = ("name")

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(name=self.kwargs.get('name'),
                            slug=self.kwargs.get('slug'))


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          ]
