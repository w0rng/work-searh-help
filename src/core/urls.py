from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include(('siteq.api.v1.urls', 'api_v1'))),
    # path('', include('siteq.pages.urls')),
]
