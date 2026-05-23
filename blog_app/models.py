from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Author(TimeStampMixin):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author_user')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.first_name

class Post(TimeStampMixin):
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, related_name='author_post')
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title

class Comment(TimeStampMixin):
    user_comment = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user_comments')
    post_comment = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='post_comments')
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE,blank=True, null=True, related_name='child_comment')

    def __str__(self) -> str:
        return self.content
