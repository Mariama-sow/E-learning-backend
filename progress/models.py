from django.db import models
from users.models import User
from course.models import Course

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    percentage = models.IntegerField(default=0)
