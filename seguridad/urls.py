from django.urls import path
from seguridad import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.acceder, name='login'),
    path('home/', views.homePage, name='home'),
    path('tablas/', views.tablas, name="tablas"),
    path('botones/', views.botones, name="botones"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
