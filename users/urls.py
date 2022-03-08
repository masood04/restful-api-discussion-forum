from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)



urlpatterns = [
    path('userlist', views.UserListView.as_view(), name='user_list'),
    path('user/<int:pk>', views.api_root, name='user-detail'),
    path('question/<int:pk>', views.api_root, name='question-detail'),
    path('signup', views.SignupUserView.as_view(), name='signup'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    
]
