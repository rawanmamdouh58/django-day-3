from django.urls import path ,include
from .views import *


urlpatterns=[
    path('', traineeList, name='traineeList'),
    path('addTrainee', addTrainee, name="addTrainee"),
    path('updateTrainee/<int:id>', updateTrainee, name="updateTrainee"),
    path('deleteTrainee/<int:id>', deleteTrainee, name="deleteTrainee"),

]