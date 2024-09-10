from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="login"),
    path('logout',views.handleLogout,name="logout"),
    path('contact',views.contact,name="contact"),
    path('profile',views.profile,name="profile"),
    path('services',views.services,name="services"),

    
]
