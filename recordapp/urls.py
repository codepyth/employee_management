from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('registration/', registration, name='registration'),
    path('login/', emp_login, name='login'),
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    path('logout/', Logout, name='logout'),
    path('admin_login/', admin_login, name='admin_login'),
    path('myexperience/', myexperience, name='myexperience'),
    path('edit_myexperience/', edit_myexperience, name='edit_myexperience'),
    path('myeducation/', my_education, name='my_education'),
    path('edit_myeducation/', edit_myeducation, name='edit_myeducation'),
    path('change_password/', change_password, name='change_password'),
    path('admin_home/', admin_home, name='admin_home'),
    path('change_passwordadmin/', change_passwordadmin, name='change_passwordadmin'),
    path('all_employees/', all_employees, name='all_employees'),
    path('delete_employee/<int:id>/', delete_employee, name='delete_employee'),
    path('edit_profile/<int:id>/', edit_profile, name='edit_profile'),
    path('edit_education/<int:id>/', edit_education, name='edit_education'),
    path('edit_experience/<int:id>/', edit_experience, name='edit_experience'),
]