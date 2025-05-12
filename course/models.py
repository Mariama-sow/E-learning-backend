from django.db import models
from users.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    date_pub = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

class Module(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)

