from django.urls import path

from app_user import views as user_views

urlpatterns = [
    path('register/', user_views.RegisterView.as_view(), name='register')
]
