from rest_framework import serializers

from users.models import CustomUser

from .models import Comment, Review, Categories, Genres, Titles


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(source='author.username')

    class Meta:
        fields = '__all__'
        model = Comment


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Categories


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Genres


class TitlesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Titles


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = CustomUser


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(source='author.username')

    class Meta:
        fields = '__all__'
        model = Review