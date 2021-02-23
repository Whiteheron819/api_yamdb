from api.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action

from .models import User
from .serializers import UserSerializer


class AdminProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    filter_backends = [filters.SearchFilter]
    search_fields = ('email', )
    lookup_field = 'username'
    permission_classes = (IsAuthenticated, )
    pagination_class = PageNumberPagination

    @action(detail=False, methods=['GET', 'PATCH'])
    def me(self, request):
        user = User.objects.get(username=request.user)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
