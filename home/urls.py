from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('login', views.login_attempt, name='login_attempt'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('project', views.project, name='project'),
]
