from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import Home, DetailPost, CreatePost

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<slug:slug>/', DetailPost.as_view(), name='post'),
    path('post_create/', CreatePost.as_view(), name='create_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
