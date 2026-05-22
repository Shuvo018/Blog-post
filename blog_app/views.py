from typing import Any

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Author, Post, Comment

# Create your views here.

class PostList(ListView):
    template_name = 'post_list.html'
    model = Post

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        return context
    
    