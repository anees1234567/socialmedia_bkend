from django.urls import path
from . import views

urlpatterns = [
    # Define URL patterns here
    path('login/', views.login_view, name='login')
]