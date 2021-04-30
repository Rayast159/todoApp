from django.urls import path, include
from .views import MyTokenObtainPairView
from todoApp import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('task', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('log', views.log, name='login'),
    path('tasks', views.start, name='start'),
    path('register', views.register, name='register'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
