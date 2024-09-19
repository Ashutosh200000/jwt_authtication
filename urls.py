from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, UserProfileListView, CustomTokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('profiles/', UserProfileListView.as_view(), name='profiles'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
