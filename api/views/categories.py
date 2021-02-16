from rest_framework.viewsets import ModelViewSet
from api.models.categories import Categories
from api.permissions import *
from api.serializers.categories import CategoriesSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class CategoriesViewSet(ModelViewSet):
    permission_classes = [ 
        IsAuthenticatedOrReadOnly,
        IsAdminUser
        ]
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    filterset_fields = ["slug", "genre__slug", "year", "name"]
    filter_backends = [filters.SearchFilter]
    search_fields = ("name")