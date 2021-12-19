from django.contrib.auth import views
from django.urls import path


app_name = 'pages'


urlpatterns = [
    path('', views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
]