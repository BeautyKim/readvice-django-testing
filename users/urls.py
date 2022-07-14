from django.urls import path, include
from . import views
# views 파일 전체를 import


urlpatterns = [
    path('users/', views.users),
    path('login', views.login),
    path('auth', include('rest_framework.urls', namespace='rest_framework'))
]
