from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters

from posts.models import Post, Group, Follow
from .serializers import PostSerializer, CommentSerializer
from .serializers import GroupSerializer, FollowSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    Публикации могут создавать и редактировать
    только авторизованные пользователи
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
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
    permission_classes = [IsAuthenticatedOrReadOnly,
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
    permission_classes = [IsAuthenticatedOrReadOnly]


class FollowViewSet(viewsets.ModelViewSet):
    """Отбираем подписки авторизованного юзера"""
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated,
                          IsOwnerOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['following__username']

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    @action(detail=True, methods=['patch'])
    def highlight(self, request, *args, **kwargs):
        follow = self.get_object()
        return Response(follow.highlighted)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
