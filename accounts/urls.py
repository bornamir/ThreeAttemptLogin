from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name = 'login'),
    path('signup',views.signup, name = 'signup'),
    path('logout', views.logout, name = 'logout'),
    path('inside', views.inside, name = 'inside'),
    path('recover',views.recover,name = 'recover')
]