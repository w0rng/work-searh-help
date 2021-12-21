from django.contrib.auth import views
from django.urls import path
from siteq.pages.user import views as user_views
from siteq.pages.features import views as feature_views
from siteq.pages.promocode import views as promocode_views
from siteq.pages.resume import views as resume_views
from siteq.pages.vacancy import views as vacancy_views

app_name = 'pages'


urlpatterns = [
    path('', feature_views.HomePage.as_view(), name='home'),
    path('login/', views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('register/', user_views.RegistrationView.as_view(), name='register'),
    path('profile/', user_views.ProfileView.as_view(), name='profile'),
    path('promocode/', promocode_views.PromocodeView.as_view(), name='promocode'),
    path('resume/', resume_views.ResumeView.as_view(), name='resume'),
    path('vacancies/', vacancy_views.VacancyView.as_view(), name='vacancies'),
    path('vacancies/all/', vacancy_views.VacancyView.as_view(), name='all_vacancies'),
]