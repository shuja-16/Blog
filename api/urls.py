from django.urls import path
from . import views

urlpatterns =[
    path("blogpost/",views.BlogPostListCreate.as_view(), name="blog-view-create"),
    path("blogpost/<int:pk>/",views.BlogPostDetail.as_view(), name="Update")
]