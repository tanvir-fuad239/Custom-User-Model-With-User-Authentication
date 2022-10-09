from django.urls import path
from App_Login import views

app_name = "App_Login"

urlpatterns = [
    
    path('', views.sign_up, name='sign_up'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.user_logout, name='logout')

]
