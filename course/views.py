from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination

from .models import Course 
from .models import Module
from .serializers import CourseSerializer
from .serializers import ModuleSerializer
from .filters import CourseFilter
from .filters import ModuleFilTer
from .permissions import IsOwnerOrAdmin,IsTeacherReadOnly

class ModuleViewset(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrAdmin,IsTeacherReadOnly]
    authentication_classes = [JWTAuthentication,BasicAuthentication]
    pagination_class = None
    filterset_class = ModuleFilTer

class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsTeacherReadOnly,IsOwnerOrAdmin]
    authentication_classes = [JWTAuthentication,BasicAuthentication ]
    lookup_field = 'id'
    pagination_class = PageNumberPagination
    filterset_class = CourseFilter
    search_fields = ['title','description']
    ordering_fields = ['title', 'date_pub']
    ordering = ['-date_pub']  # tri par défaut


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


    
    
     