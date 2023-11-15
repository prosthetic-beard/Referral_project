
from django.urls import path, include
from .views import home, Login, withdraw, referrals, logout_view, profile, how, tasks, signup, first_login, second_login, third_login, fourth_login, delete_withdrawal, index, ResetPasswordView, FileDownloadView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy


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
    path('password-reset', ResetPasswordView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', success_url = reverse_lazy('base:password_reset_complete')),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    
    
    path('download/<str:file_name>/', FileDownloadView.as_view(), name='file_download'),

]