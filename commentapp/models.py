from django.db import models
from articleapp.models import Article
from django.contrib.auth.models import User

# Create your models here.


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='comment')

    content = models.CharField(max_length=1024, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
