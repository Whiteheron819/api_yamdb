from rest_framework.viewsets import ModelViewSet
from api.models.titles import Titles
from api.permissions import *
from api.serializers.titles import TitlesSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TitlesViewSet(ModelViewSet):
    permission_classes = [ 
        IsAuthenticatedOrReadOnly,
        IsAdminUser
        ]
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["slug"]
