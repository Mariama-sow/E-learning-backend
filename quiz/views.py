from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from rest_framework.pagination import PageNumberPagination
from course.permissions import IsOwnerOrAdmin
from course.permissions import IsTeacherReadOnly

from .models import Question
from .models import Quiz
from .models import Answer
from .models import UserAnswer

from .serializers import QuestionSerializer
from .serializers import QuizSerializer
from .serializers import AnswerSerializer
from .serializers import UserAnswerSerializer

class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsTeacherReadOnly,IsOwnerOrAdmin,
                          IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication, BasicAuthentication]

class QuizViewset(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsTeacherReadOnly,IsOwnerOrAdmin,
                          IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication , BasicAuthentication]

class AnswerViewset(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class UserAnswerViewset(viewsets.ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
