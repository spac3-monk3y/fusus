from django.urls import path
from .views import UserGroupsView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='auth_jwt_get'),
    path('groups/', UserGroupsView.as_view(), name='auth_user_groups'),
    path('token/refresh/', TokenRefreshView.as_view(), name='auth_jwt_refresh'),
]
