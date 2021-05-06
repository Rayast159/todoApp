from django.urls import path, include
from .views import MyTokenObtainPairView
from todoApp import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('task', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login', views.log, name='login'),
    path('start', views.start, name='start'),
    path(r'tasks/(?P<id>[0-9]+)/(?P<token_refresh>[^/]+)/(?P<token_access>[^/]+)', views.tasks, name='tasks'),
    path('register', views.register, name='register'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('django-rq/', include('django_rq.urls')),
]
