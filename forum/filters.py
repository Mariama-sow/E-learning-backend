from django_filters.rest_framework import filters , FilterSet
from .models import ForumThread
from .models import ForumReply

class ForumThreadFilters(FilterSet):
    course = filters.CharFilter(field_name='course__title',lookup_expr='icontains')

    class Meta:
        model = ForumThread
        fields = ('course','title')