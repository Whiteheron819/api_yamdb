from rest_framework.viewsets import ModelViewSet
from api.models.titles import Titles
from .permissions import *
from api.serializers import T


class TitlesViewSet(ModelViewSet):
    pass