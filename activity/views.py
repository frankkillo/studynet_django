from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from course.serializers import CourseListSerializer
from course.models import Course, Lesson
from .serializers import ActivitySerializer
from .models import Activity


@api_view(['GET'])
def get_active_courses(request):
    courses = set(activity.course for activity in request.user.activities.all() if activity.status == activity.STARTED)
    serializer = CourseListSerializer(courses, many=True, context={'request': request})

    return Response(serializer.data)


@api_view(['POST'])
def activity_started(request):
    course = get_object_or_404(Course, slug=request.data.get('course_slug', ''))
    lesson = get_object_or_404(Lesson, slug=request.data.get('lesson_slug', ''))

    activity, _ = Activity.objects.get_or_create(course=course, lesson=lesson, created_by=request.user)

    serializer = ActivitySerializer(activity)

    return Response(serializer.data)


@api_view(['POST'])
def mark_as_done(request):
    course = get_object_or_404(Course, slug=request.data.get('course_slug', ''))
    lesson = get_object_or_404(Lesson, slug=request.data.get('lesson_slug', ''))

    activity = Activity.objects.get(course=course, lesson=lesson, created_by=request.user)
    activity.status = Activity.DONE
    activity.save()

    serializer = ActivitySerializer(activity)

    return Response(serializer.data)