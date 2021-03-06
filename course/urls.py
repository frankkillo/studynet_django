from django.urls import path

from course import views


urlpatterns = [
    path('', views.get_courses),
    path('front-courses/', views.get_front_courses),
    path('categories/', views.get_categories),
    path('<slug:slug>/', views.get_course),
    path('<slug:course_slug>/<slug:lesson_slug>/', views.add_comment),
    path('<slug:course_slug>/<slug:lesson_slug>/comments/', views.get_comments),
    path('<slug:course_slug>/<slug:lesson_slug>/quiz/', views.get_quiz),
]