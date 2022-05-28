from versatileimagefield.serializers import VersatileImageFieldSerializer

from rest_framework import serializers

from .models import Category, Course, Lesson, Comment, Quiz


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "slug",
        ]


class CourseListSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes= [
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__300x500')
        ]
    )
    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "slug",
            "image",
            "short_description",
            "created_at",
        ]

    
class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "slug",
            "short_description",
            "long_description",
            "created_at",
        ]


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            "id",
            "title",
            "slug",
            "type",
            "short_description",
            "long_description",
            "youtube_id",
        ]


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = [
            "id",
            "lesson",
            "question",
            "answer",
            "ops_1",
            "ops_2",
            "ops_3",
        ]


class CommentSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Comment
        fields = [
            "id",
            "content",
            "created_at",
            "created_by",
        ]
