
from django.urls import path, include
from .views import home, Login, withdraw, referrals, logout_view, profile, how, tasks, signup, first_login, second_login, third_login, fourth_login, delete_withdrawal, index

app_name = 'base'

urlpatterns = [
    path('', index, name='index' ),
    path('register', signup, name='signup' ),
    path('login', Login, name='login' ),
    path('first_app', first_login, name='first-login' ),
    path('second_app', second_login, name='second-login' ),
    path('third_app', third_login, name='third-login' ),
    path('fourth_app', fourth_login, name='fourth-login' ),
    path('dashboard', home, name='home'),
    path('withdraw', withdraw, name='withdraw'),
    path('delete-withdrawal/<int:id>', delete_withdrawal, name='delete-withdraw'),
    path('referrals', referrals, name='referrals'),
    path('profile', profile, name='profile'),
    path('how', how, name='how'),
    path('tasks', tasks, name='tasks'),
    path('logout', logout_view, name='logout'),

]