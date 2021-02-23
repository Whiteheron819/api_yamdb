from rest_framework.permissions import IsAuthenticated
from api.permissions import AdminPermission
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
    permission_classes = (AdminPermission, )
    pagination_class = PageNumberPagination

    @action(detail=False, permission_classes=[IsAuthenticated])
    def me(self, request):
        user = User.objects.get(username=request.user)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data)
        elif request.method == 'PATCH':
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
