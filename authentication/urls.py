from django.urls import path

from authentication import views


urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('user/', views.UserMe.as_view(), name='me'),
    path('activate-user/', views.VerifyUserView.as_view(), name='me'),
]