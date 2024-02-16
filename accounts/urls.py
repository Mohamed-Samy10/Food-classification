from django.urls import path 
from . import views
from django.contrib.auth.views import PasswordChangeDoneView
from . import api


urlpatterns = [
    path('main/',views.main,name='main'),
    path('',views.custom_login_view, name='login'),
    path('register/',views.register,name='register'),
    path('profile/', views.view_profile, name='profile'),
    path('password_change/',views.custom_password_change,name='password_change' ),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('api/register/', api.register_user, name='register'),
    path('api/login/', api.user_login, name='login'),
    path('api/logout/', api.user_logout, name='logout'),
    path('api/change_password/', api.change_password, name='change_password'),
    path('api/profile/', api.getProfile, name='get_profile'),
]
