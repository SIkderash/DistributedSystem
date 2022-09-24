from django.urls import path, re_path
from stories import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^addStory/$', views.addStory),
    re_path(r'^imageUpload/$', views.imageUpload),
    re_path(r'^stories/$', views.getStories),

    re_path(r'^addStatus/$', views.addStatus),
    re_path(r'^feed/$', views.getFeed),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 