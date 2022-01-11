from rest_framework import serializers
from posts.models import Post, Comment, Group, User, Follow


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        ref_name = 'ReadOnlyUsers'


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(
        read_only=True,
        slug_field='following',
        default=serializers.CurrentUserDefault())
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='follower',
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Follow
        fields = '_all_'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'text', 'created')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault())

    class Meta:
        fields = '__all__'
        read_only_fields = ('author',)
        model = Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('title', 'slug', 'description', 'posts')