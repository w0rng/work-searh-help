from django.contrib.auth import views
from django.urls import path
from siteq.pages.user import views as user_views
from siteq.pages.features import views as feature_views
from siteq.pages.promocode import views as promocode_views
from siteq.pages.resume import views as resume_views
from siteq.pages.vacancy import views as vacancy_views
from siteq.pages.subscription import views as subscription_views
from siteq.pages.module import views as modules_views
from siteq.pages.analyze import views as analyze_views

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
    path('subscriptions/', subscription_views.SubscriptionView.as_view(), name='subscriptions'),
    path('subscribe/', subscription_views.SubscriptionCreateView.as_view(), name='subscribe'),
    path('modules/', modules_views.ModuleView.as_view(), name='modules'),
    path('modules/save/', modules_views.UpdateModuleView.as_view(), name='modules_save'),
    path('analyze/test/', analyze_views.EditorChartView.as_view(), name='analyze_views'),
]
