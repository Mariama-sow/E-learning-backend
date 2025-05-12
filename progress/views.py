from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Progress
from .serializers import ProgressSerializer

class ProgressViewset(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    authentication_classes = [BasicAuthentication,JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]