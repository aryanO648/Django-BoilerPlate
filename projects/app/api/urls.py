from django.urls import path
from .views import register_user, LoginUser,  LogoutUser

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', LoginUser.as_view(), name='login_user'),
    path('logout/', LogoutUser.as_view(), name='logout_user'),
]
