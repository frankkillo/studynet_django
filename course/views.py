from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Course, Comment, Lesson, Category, Quiz
from .serializers import (
    CourseListSerializer, 
    CourseDetailSerializer, 
    LessonListSerializer, 
    CommentSerializer,
    CategorySerializer,
    QuizSerializer,
)


@api_view(['GET'])
@permission_classes([])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([])
def get_courses(request):
    category_id = request.GET.get('category_id')
    courses = Course.objects.all()
    if category_id:
        courses = courses.filter(categories__in=[int(category_id)])
    serializer = CourseListSerializer(courses, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([])
def get_front_courses(request):
    courses = Course.objects.all()[:4]
    serializer = CourseListSerializer(courses, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([])
def get_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.user.is_authenticated:
        lesson_serializer = LessonListSerializer(course.lessons.all(), many=True)
        course_serializer = CourseDetailSerializer(course)
        course_data = course_serializer.data
        lesson_data = lesson_serializer.data
    else:
        course_data = {}
        lesson_data = course.lessons.values("title")

    return Response({
        'course': course_data,
        'lessons': lesson_data
    })


@api_view(['GET'])
def get_quiz(request, course_slug, lesson_slug):
    lesson = get_object_or_404(Lesson, slug=lesson_slug)
    serializer = QuizSerializer(lesson.quizzes.first())
    return Response(serializer.data)


@api_view(['GET'])
def get_comments(request, course_slug, lesson_slug):
    lesson = get_object_or_404(Lesson, slug=lesson_slug)
    serializer = CommentSerializer(lesson.comments.all(), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_comment(request, course_slug, lesson_slug):
    comment_data = {
        'course': get_object_or_404(Course, slug=course_slug),
        'lesson': get_object_or_404(Lesson, slug=lesson_slug),
        'content': request.data.get('content'),
        'created_by': request.user
    }
    comment = Comment.objects.create(**comment_data)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)