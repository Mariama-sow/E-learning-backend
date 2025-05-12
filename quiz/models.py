from django.db import models

from course.models import Course
from users.models import User

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    QUESTION_TYPES = [
        ('qcm', 'Choix Multiple'),
        ('vf', 'Vrai ou Faux'),
        ('texte', 'Texte Libre'),
    ]
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    content = models.TextField()
    type = models.CharField(max_length=10, choices=QUESTION_TYPES, default='qcm')

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    is_correct = models.BooleanField(default=False)

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
