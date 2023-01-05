from django.db import models
from .manager import CustomUser


class Teacher(models.Model):
    username = models.OneToOneField(CustomUser, unique=True, on_delete=models.CASCADE, related_name='teacher')
    image = models.ImageField(default='default.jpg', blank=True, null=True)
    job_title = models.CharField(max_length=5)
    subject_id = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.username.username} {self.username.name} ({self.username.surname})"
