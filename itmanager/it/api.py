from it.models import It
from rest_framework import viewsets, permissions
from .serializers import ItSerializer

#It ViewSet
class ItViewSet(viewsets.ModelViewSet):
    queryset = It.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = ItSerializer