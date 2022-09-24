from django.urls import path, re_path
from authentication import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^auth/register/$', views.register),
    re_path(r'^auth/user/$', views.userView),
    re_path(r'^auth/login/$', views.login),
    re_path(r'^auth/logout/$', views.logout),
    path('auth/verify/<uid>' , views.verify),
    re_path(r'^auth/api_call/$', views.api_call)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 