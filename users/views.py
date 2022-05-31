from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from stats.models import Statistics
from users.serializers import UserSerializer, UserRegisterSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.action == 'create':
            serializer = UserRegisterSerializer
        return serializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'list':
            queryset = get_user_model().objects.exclude(id=self.request.user.id)
        return queryset

    def perform_create(self, serializer):
        user = serializer.save()
        Statistics.objects.create(id=user.id, user=user)

    @action(detail=False, methods=['GET'], name='me')
    def me(self, request):
        me = get_user_model().objects.get(id=request.user.id)
        return Response(self.get_serializer(me).data)
