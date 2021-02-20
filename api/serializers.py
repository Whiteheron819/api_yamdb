from rest_framework import serializers

from users.models import CustomUser

from .models import Comment, Review, Category, Genre, Title


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(source='author.username')


    class Meta:
        fields = '__all__'
        model = Comment


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        fields = ['name', 'slug']
        model = Category


class GenreSerializer(serializers.ModelSerializer):


    class Meta:
        fields = ['name', 'slug']
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    score = serializers.FloatField(read_only=True)
    category = serializers.SlugRelatedField(read_only=True,
                                            slug_field='name'
                                            )
    genre = serializers.SlugRelatedField(read_only=True,
                                         slug_field='name'
                                         )

    class Meta:
        fields = ('id', 'name', 'year', 'category', 'genre', 'score',  )
        model = Title


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = CustomUser


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(source='author.username')
    
    class Meta:
        fields = '__all__'
        model = Review
