from django.urls import path, re_path
from users import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^register/$', views.register),
    re_path(r'^user/$', views.userView),
    re_path(r'^login/$', views.login),
    re_path(r'^logout/$', views.logout),
    path('verify/<uid>' , views.verify),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 