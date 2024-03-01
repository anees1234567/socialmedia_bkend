from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView;

urlpatterns = [
    # Define URL patterns here
    path('login/', views.login_view, name='login')
]