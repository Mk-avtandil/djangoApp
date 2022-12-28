from django.urls import path

from .views import logout_user, RegisterUser, LoginUser


urlpatterns = [
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
