from django.urls import path, re_path
from Story import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^status/addStatus/$', views.addStatus),
    re_path(r'^status/feed/$', views.getFeed),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 