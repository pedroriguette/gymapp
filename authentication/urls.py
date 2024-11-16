from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.urls import path


urlpatterns = [
    path('api/v1/authentication/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('api/v1/authentication/token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('api/v1/authentication/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
