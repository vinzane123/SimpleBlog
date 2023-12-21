"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import (AuthorDetailView, CommetDetailView,
                        CommentListCreateView, BlogDetailView,
                        BlogPostListCreateView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/authors/<int:pk>/',
         AuthorDetailView.as_view(),
         name='author-detail'),
    path('api/v1/posts/', BlogPostListCreateView.as_view(), name='post-list'),
    path('api/v1/posts/<int:pk>/',
         BlogDetailView.as_view(),
         name='post-detail'),
    path('api/v1/posts/<int:pk>/comments/',
         CommentListCreateView.as_view(),
         name='comment-list'),
    path('api/v1/posts/<int:pk>/comments/<int:comment_pk>/',
         CommetDetailView.as_view(),
         name='comment-detail'),
]
