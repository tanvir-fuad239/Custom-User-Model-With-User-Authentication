from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('App_Login.urls')),
    path('', views.index, name='index'),
    path('home/', views.main_home, name='main_home')
]
