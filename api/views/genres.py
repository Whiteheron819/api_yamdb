from rest_framework.viewsets import ModelViewSet
from api.models.genres import Genres
from api.permissions import *
from api.serializers.genres import GenresSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class GenresViewSet(ModelViewSet):
    permission_classes = [ 
        IsAuthenticatedOrReadOnly,
        IsAdminUser
        ]
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    filterset_fields = ["name"]
    filter_backends = [filters.SearchFilter]
    search_fields = ("name")
