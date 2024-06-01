from rest_framework import generics,status
from .models import BlogPost
from .serializers import BlogPostSerializer
from api.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response


class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"detail": "Sorry, no blogs to show"}, status=status.HTTP_200_OK)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        slug = self.kwargs.get(self.lookup_field)
        obj = generics.get_object_or_404(queryset, slug=slug)
        self.check_object_permissions(self.request, obj)
        return obj
