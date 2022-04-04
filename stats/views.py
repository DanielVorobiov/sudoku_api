from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from stats.models import Statistics
from stats.serializers import StatisticsSerializer


class StatisticsViewSet(GenericViewSet, ListModelMixin, UpdateModelMixin, CreateModelMixin):
    serializer_class = StatisticsSerializer
    queryset = Statistics.objects.all()
    permission_classes = [AllowAny]

