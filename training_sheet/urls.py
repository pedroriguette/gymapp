from django.urls import path
from . import views


urlpatterns = [
    path('trainingsheets/list/', views.TrainingSheetListview.as_view(), name='training_sheet_list'),
    path('trainingsheets/create/', views.TrainingSheetCreateView.as_view(), name='training_sheet_create'),
    path('trainingsheets/<int:pk>/update/', views.TrainingSheetUpdateView.as_view(), name='training_sheet_update'),
    path('trainingsheets/<int:pk>/delete/', views.TrainingSheetDeleteView.as_view(), name='training_sheet_delete'),

    path('api/v1/trainingsheets/', views.TrainingSheetListCreateAPIView.as_view(), name='trainingsheet-list-create-api'),
    path('api/v1/trainingsheets/<int:pk>/', views.TrainingSheetRetrieveUpdateDestroyAPIView.as_view(), name='trainingsheet-detail-update-destroy-api'),
]
