from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project

id = get_user_model()

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True, blank=True)
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    like = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} - {self.writer} --- {self.created_at}'

