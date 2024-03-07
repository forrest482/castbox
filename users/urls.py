from django.urls import path
from .views import UserProfileView, UserProfileListView, UserProfileDetailView, CreateUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profiles/', UserProfileListView.as_view(), name='user-profile-list'),
    path('profiles/<str:username>/', UserProfileDetailView.as_view(),
         name='user-profile-detail'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
