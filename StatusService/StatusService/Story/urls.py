from django.urls import path, re_path
from Story import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^story/addStory/$', views.addStory),
    re_path(r'^story/stories/$', views.getStories),
    re_path(r'^story/story/$', views.showStories),
    #path('story/story/<uid>' , views.showStories),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 