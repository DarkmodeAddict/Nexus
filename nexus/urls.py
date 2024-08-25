from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('nex_like/<int:pk>', views.nex_like, name='nex_like'),
    path('nex_show/<int:pk>', views.nex_show, name='nex_show'),
    path('unfollow/<int:pk>', views.unfollow, name='unfollow'),
    path('follow/<int:pk>', views.follow, name='follow')
]
