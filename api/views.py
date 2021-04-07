from rest_framework import viewsets

from .serializers import ccsSerializer
from .models import ccsFormData


class ccsViewSet(viewsets.ModelViewSet):
    queryset = ccsFormData.objects.all().order_by('lastName')
    serializer_class = ccsSerializer
