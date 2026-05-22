from django.urls import path
from blog_app import views
urlpatterns = [
    path('', view=views.PostList.as_view(), name='post_list'),
]
