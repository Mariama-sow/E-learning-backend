from rest_framework import serializers

from .models import Course , Module

class CourseSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'creator', 'date_pub', 'image')
        read_only_fields = ('date_pub','creator')


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = ('id', 'title', 'content', 'course', 'pdf')
        read_only_fields = ('course',)