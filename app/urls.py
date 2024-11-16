from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', include('exercises.urls')),
    path('', include('muscle_groups.urls')),
    path('', include('coaches.urls')),
    path('', include('students.urls')),
    path('', include('training_sheet.urls')),

    path('', include('authentication.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
