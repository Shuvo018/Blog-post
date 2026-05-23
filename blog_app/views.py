from typing import Any

from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from .models import Author, Post, Comment
from .forms import PostForm, CommentForm
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
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.post_comments.all()
        return context

def CreateComment(request, pk):
    post = Post.objects.get(id=int(pk))
    form = CommentForm()
    
    comments = post.post_comments.all()
    print(comments)
    if request.method == "POST":
        comment_content = request.POST.get('content')
        # print(request.user)
        Comment.objects.create(
            user_comment = request.user,
            post_comment = post,
            content = comment_content,
            parent = None,
        )
        # print(comment_content)

    return render(request=request, template_name='post_detail.html', context={'form': form, 'post': post, 'comments': comments})

def addReply(request, comment_id):
    parent_comment = Comment.objects.get(id=comment_id)
    form = CommentForm()
    if request.method == 'POST':
        reply_content = request.POST.get('content')

        Comment.objects.create(
            user_comment = request.user,
            post_comment = parent_comment.post_comment,
            parent = parent_comment,
            content = reply_content,
        )
        return redirect('post_detail', pk=parent_comment.post_comment.pk)
    return render(request=request, template_name='comment_reply.html', context={'form': form, 'parent_comment': parent_comment})