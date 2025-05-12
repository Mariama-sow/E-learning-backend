from django.db import models
from users.models import User

class Badge(models.Model):
    name = models.CharField(max_length=255)
    condition = models.TextField()

class UserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)

