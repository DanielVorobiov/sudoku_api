from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from stats.models import Statistics
from stats.serializers import StatisticsSerializer


class StatisticsViewSet(GenericViewSet, ListModelMixin, UpdateModelMixin, CreateModelMixin, RetrieveModelMixin):
    serializer_class = StatisticsSerializer
    queryset = Statistics.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'my_statistics':
            queryset = Statistics.objects.filter(user=self.request.user)
        return queryset

    @action(detail=False, methods=['GET'], name='my-statistics', url_path='my-statistics')
    def my_statistics(self, request):
        stats = self.get_queryset().first()
        return Response(self.get_serializer(stats).data)
