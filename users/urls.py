from django.urls import path, include
# from django.contrib.auth.views import login
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'

urlpatterns = [
    # Login page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),

    # Logout page
    path('logout/', views.logout_view, name='logout'),

    # register page
    path('register/',views.register,name='register')

]