from django.urls import path
from .views import TaskDetailView,TaskListCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name='task-list'),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name='task-detail'),
    path('tasks/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tasks/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]