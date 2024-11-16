from django.urls import path
from . import views


urlpatterns = [
    path('exercises/list/', views.ExerciceListView.as_view(), name='exercice_list'),
    path('exercises/create/', views.ExerciceCreateView.as_view(), name='exercice_create'),
    path('exercices/<int:pk>/update/', views.ExerciceUpdateView.as_view(), name='exercice_update'),
    path('exercises/<int:pk>/detail/', views.ExerciceDetailView.as_view(), name='exercice_detail'),
    path('exercises/<int:pk>/delete', views.ExerciceDeleteView.as_view(), name='exercice_delete'),

    path('api/v1/exercises/', views.ExerciceListCreateAPIView.as_view(), name='exercice-list-create-api'),
    path('api/v1/exercises/<int:pk>/', views.ExerciceRetrieveUpdateDestroyAPIView.as_view(), name='exercice-detail-update-destroy-api'),
]
