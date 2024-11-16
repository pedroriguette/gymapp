from django.urls import path
from . import views


urlpatterns = [
    path('coaches/list/', views.CoachListView.as_view(), name='coach_list'),
    path('coaches/create/', views.CoachCreateView.as_view(), name='coach_create'),
    path('coaches/<int:pk>/detail/', views.CoachDetailView.as_view(), name='coach_detail'),
    path('coaches/<int:pk>/update/', views.CoachUpdateView.as_view(), name='coach_update'),
    path('coaches/<int:pk>/delete/', views.CoachDeleteView.as_view(), name='coach_delete'),

    path('api/v1/coaches/', views.CoachListCreateAPIView.as_view(), name='coach-list-create-api'),
    path('api/v1/coaches/<int:pk>/', views.CoachRetrieveUpdateDestroyAPIView.as_view(), name='coach-detail-update-destroy-api'),
]
