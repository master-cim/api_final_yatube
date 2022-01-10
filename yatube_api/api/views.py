from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group
from .serializers import PostSerializer, CommentSerializer, GroupSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    Публикации могут создавать и редактировать
    только авторизованные пользователи
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        # IsAuthenticated,
                          IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['patch'])
    def highlight(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(post.highlighted)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Отбираем только нужные комментарии к посту"""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,
                          IsOwnerOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments

    @action(detail=True, methods=['patch'])
    def highlight(self, request, *args, **kwargs):
        comment = self.get_object()
        return Response(comment.highlighted)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Группы можно только просматривать"""
    serializer_class = GroupSerializer
    queryset = Group.objects.all()