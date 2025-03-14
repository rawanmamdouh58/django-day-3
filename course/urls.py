from django.urls import path ,include
from .views import *


urlpatterns = [
    path('', courseList, name='courseList'),
    path('addCourse', addCourse, name="addCourse"),
    path('updateCourse/<int:id>', updateCourse, name="updateCourse"),
    path('deleteCourse/<int:id>', deleteCourse, name="deleteCourse"),
    # Add this new path
    path('trainees/<int:course_id>', courseTrainees, name='courseTrainees'),
]