from django.urls import path
from . import views


urlpatterns = [
    path('students/list/', views.StudentListView.as_view(), name='student_list'),
    path('students/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/detail/', views.StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/update/', views.StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),

    path('api/v1/students/', views.StudentListCreateAPIView.as_view(), name='student-list-create-api'),
    path('api/v1/students/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-detail-update-destroy-api'),
]
