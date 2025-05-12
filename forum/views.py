from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import ForumThread
from .models import ForumReply
from .serializers import ForumThreadSerialzer
from .serializers import ForumReplySerializer
from .filters import ForumThreadFilters

class ForumThreadViewset(viewsets.ModelViewSet):
    queryset = ForumThread.objects.all()
    serializer_class = ForumThreadSerialzer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [BasicAuthentication,JWTAuthentication]
    filterset_class = ForumThreadFilters

class ForumReplyViewset(viewsets.ModelViewSet):
    queryset = ForumReply.objects.all()
    serializer_class = ForumReplySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [BasicAuthentication,JWTAuthentication]