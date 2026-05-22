from django.urls import path
from blog_app import views
urlpatterns = [
    path('', view=views.PostList.as_view(), name='post_list'),
    path('post-create/', view=views.PostCreateView.as_view(), name='post_create'),
    path('post-detail/<int:pk>', view=views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comment', view=views.CreateComment, name='create_comment'),
    path('post/<int:pk>/comment/<int:pk>', view=views.CreateComment, name='comment_reply'),
]
