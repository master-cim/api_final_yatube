from rest_framework import serializers
from posts.models import Post, Comment, Group, User, Follow
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)
        ref_name = 'ReadOnlyUsers'


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username')
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault())

    def validate(self, data):
        """
        Проверяем что юзер не подписывается на себя.
        """
        if data['following'] == self.context['request'].user:
            raise serializers.ValidationError(
                'Нельзя подписываться на себя!'
            )
        return data

    class Meta:
        model = Follow
        exclude = ('id',)
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following'],
                message='Подписка на автора уже есть!'
            )
        ]


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
        fields = ('title', 'slug', 'description')
