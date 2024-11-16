from django.urls import path
from . import views


urlpatterns = [
    path('musclegroups/list/', views.MuscleGroupListView.as_view(), name='muscle_group_list'),
    path('musclegroups/create/', views.MuscleGroupCreateView.as_view(), name='muscle_group_create'),
    path('musclegroups/<int:pk>/delete/', views.MuscleGroupDeleteView.as_view(), name='muscle_group_delete'),

    path('api/v1/musclegroups/', views.MuscleGroupListCreateAPIView.as_view(), name='musclegroup-list-create-api'),
    path('api/v1/musclegroups/<int:pk>/', views.MuscleGroupDestroyAPIView.as_view(), name='musclegroup-destroy-api'),
]
