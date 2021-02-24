from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.permissions import (IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import ModelFilter
from .models import Category, Comment, Genre, Review, Title
from .permissions import AdminPermission, GeneralPermission, ReviewPermission, \
    ModeratorPermission
from .serializers import (CategoriesSerializer, CommentSerializer,
                          GenreSerializer, ReviewSerializer,
                          TitleGeneralSerializer, TitleSlugSerializer)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    lookup_field = 'slug'
    serializer_class = GenreSerializer
    permission_classes = [GeneralPermission]

    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    lookup_field = 'slug'
    serializer_class = CategoriesSerializer
    permission_classes = [GeneralPermission]

    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class TitleViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filter_class = ModelFilter
    permission_classes = [GeneralPermission]

    def get_serializer_class(self):
        if self.action in ('create', 'partial_update'):
            return TitleSlugSerializer
        return TitleGeneralSerializer

    def get_queryset(self):
        return Title.objects.all().annotate(rating=Avg('reviews__score'))


class ReviewViewSet(ModelViewSet):
<<<<<<< HEAD
    queryset = Review.objects.all()
=======
>>>>>>> 85697e6c9e577da27ff30178f7c59187daf19d48
    filter_backends = [DjangoFilterBackend]
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

<<<<<<< HEAD
=======
    def get_permissions(self):
        if self.action == 'partial_update':
            permission_classes = [ReviewPermission]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticatedOrReadOnly,
                                  ModeratorPermission]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]

>>>>>>> 85697e6c9e577da27ff30178f7c59187daf19d48
    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
<<<<<<< HEAD
        serializer.save(author=self.request.user, title=title)
=======
        if serializer.is_valid():
            serializer.save(author=self.request.user,
                            title=title,
                            text=self.request.data['text'],
                            score=self.request.data['score'])


class CommentViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action == 'partial_update':
            permission_classes = [ReviewPermission]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticatedOrReadOnly,
                                  ModeratorPermission]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        if serializer.is_valid():
            serializer.save(author=self.request.user,
                            review=review,
                            text=self.request.data['text'])
>>>>>>> 85697e6c9e577da27ff30178f7c59187daf19d48
