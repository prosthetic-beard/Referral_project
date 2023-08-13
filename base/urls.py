
from django.urls import path, include
from .views import home, Login, withdraw, referrals, logout_view, profile, how, tasks

app_name = 'base'

urlpatterns = [
    path('', Login, name='login' ),
    path('dashboard', home, name='home'),
    path('withdraw', withdraw, name='withdraw'),
    path('referrals', referrals, name='referrals'),
    path('profile', profile, name='profile'),
    path('how', how, name='how'),
    path('tasks', tasks, name='tasks'),
    path('logout', logout_view, name='logout'),

]