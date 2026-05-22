from typing import Any

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from .models import Author, Post, Comment
from .forms import PostForm
# Create your views here.

class PostList(ListView):
    template_name = 'post_list.html'
    model = Post

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        return context
    
class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm

    success_url = '/'

class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post
    context_object_name = 'post'