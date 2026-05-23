from django.urls import path
from blog_app import views

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', view=views.PostList.as_view(), name='post_list'),
    path('post-create/', view=views.PostCreateView.as_view(), name='post_create'),
    path('post-detail/<int:pk>', view=views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comment', view=views.CreateComment, name='create_comment'),
    path('comment/<int:comment_id>/reply', view=views.addReply, name='comment_reply'),

    path('registration/', view=views.UserRegistrationView.as_view(), name='registration'),
    path('login/', view=LoginView.as_view(), name='login'),
]
