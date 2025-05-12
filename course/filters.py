from django_filters.rest_framework import FilterSet , filters
from .models import Course
from .models import Module

class CourseFilter(FilterSet):
    title = filters.CharFilter( lookup_expr='icontains')
    creator = filters.CharFilter(field_name='creator__username',lookup_expr='icontains')
    class Meta:
        model = Course
        fields = ['title', 'creator']

class ModuleFilTer(FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    course  = filters.NumberFilter()

    class Meta:
        model = Module 
        fields = ['title','course']