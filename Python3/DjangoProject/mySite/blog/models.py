from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class BlogArticles(models.Model):
    title = models.CharField(max_length=300)  # 1规定了字段title的属性类型韦CharField()类型，
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")  # 2
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:  # 3
        ordering = ("-publish", )

    def __str__(self):
        return self.title
