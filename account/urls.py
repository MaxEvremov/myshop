from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login


urlpatterns = [
  # path('login/', views.user_login, name='login'),
  path('login/', 
        LoginView.as_view(),
        name="login"
    ),
  path('logout/', 
        LogoutView.as_view(), 
        name="logout"
    ),
  path('logout-then-login/', 
        logout_then_login, 
        # name="logout_then_login"
    ),
  path('', views.dashboard, name='dashboard'),
]
