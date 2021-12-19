from django.contrib.auth import views
from django.urls import path
from pages.user import views as user_views
from pages.features import views as feature_views
from pages.promocode import views as promocode_views


app_name = 'pages'


urlpatterns = [
    path('', feature_views.HomePage.as_view(), name='home'),
    path('login/', views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('register/', user_views.RegistrationView.as_view(), name='register'),
    path('profile/', user_views.ProfileView.as_view(), name='profile'),
    path('promocode/', promocode_views.PromocodeView.as_view(), name='promocode'),
]
