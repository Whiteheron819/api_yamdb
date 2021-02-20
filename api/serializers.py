from rest_framework import serializers

from users.models import CustomUser

from .models import Comment, Review, Category, Genre, Title


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(source='author.username')

    class Meta:
        fields = '__all__'
        model = Comment


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug',)


class TitleSlugSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(many=True, slug_field='slug', queryset=Genre.objects.all())
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())

    class Meta:
        model = Title
        fields = '__all__'


class TitleGeneralSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    category = CategoriesSerializer()
    rating = serializers.FloatField()

    class Meta:
        model = Title
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = CustomUser


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(source='author.username')

    class Meta:
        fields = '__all__'
        model = Review
