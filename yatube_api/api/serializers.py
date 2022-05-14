from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from django.contrib.auth import get_user_model
from posts.models import Comment, Post, Group, Follow

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description',)


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True, )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True,)
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all(),)

    def validate(self, data):
        user = self.context['request'].user
        following = data['following']
        if user == following:
            raise serializers.ValidationError('Подписаться на себя нельзя')
        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError('Подписка уже существует')
        return data

    class Meta:
        model = Follow
        fields = ('user', 'following')
