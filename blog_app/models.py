from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Author(TimeStampMixin):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.first_name

class Post(TimeStampMixin):
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, name='author_post')
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title

class Comment(TimeStampMixin):
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, name='author_comment')
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, name='post_comment')
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self) -> str:
        return self.content