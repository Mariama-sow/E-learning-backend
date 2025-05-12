from rest_framework import serializers
from .models import ForumThread , ForumReply

class ForumThreadSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ForumThread
        fields = ('id', 'course', 'title', 'author', 'created_at')

class ForumReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumReply
        fields = ('id', 'thread', 'author', 'content', 'created_at')
