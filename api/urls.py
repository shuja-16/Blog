from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BlogPostListCreateView, BlogPostDetailView

urlpatterns = [
    path('blogposts/', BlogPostListCreateView.as_view(), name='blogpost-list-create'),
    path('blogposts/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('blogposts/<slug:slug>/', BlogPostDetailView.as_view(), name='blog_post_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)