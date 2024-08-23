from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('profile/', views.profile, name='profile'),
    path('school/', views.school, name='school'),
    path('template/', views.template, name='template'),
    path('school.html/', views.school.html, name='school.html'),
    path('profile.html/', views.profile.html, name='profile.html'),
]