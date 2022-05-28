from django.urls import path

from . import views


urlpatterns = [
    path('get-active-courses/', views.get_active_courses),
    path('activity-started/', views.activity_started),
    path('mark-as-done/', views.mark_as_done)
]