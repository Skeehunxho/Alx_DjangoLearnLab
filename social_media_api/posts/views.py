from rest_framework import viewsets, permissions, decorators, response, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Post, Comment
from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("author").prefetch_related("comments")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["author"]  # /posts/?author=<user_id>
    search_fields = ["title", "content"]  # /posts/?search=hello
    ordering_fields = ["created_at", "updated_at", "title"]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["retrieve"]:
            return PostDetailSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @decorators.action(detail=True, methods=["get"])
    def comments(self, request, pk=None):
        post = self.get_object()
        qs = post.comments.select_related("author")
        page = self.paginate_queryset(qs)
        ser = CommentSerializer(page or qs, many=True)
        if page is not None:
            return self.get_paginated_response(ser.data)
        return response.Response(ser.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("post", "author")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # Filter comments by post and/or author: /comments/?post=1&author=2
    filterset_fields = ["post", "author"]
    search_fields = ["content"]
    ordering_fields = ["created_at", "updated_at"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
