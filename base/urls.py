
from django.urls import path, include
from .views import home, Login

app_name = 'base'

urlpatterns = [
    path('', Login, name='login' ),
    path('dashboard', home, name='home'),

]