from django.urls import path
from .views import UserRegistrationView, LoginView, UserLogoutView  

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='user-login') ,
    path('logout/', UserLogoutView.as_view(), name='logout'),

]