from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),

    path('user/<str:pk>/', views.user_page,
         name='profile'),
    path('account/', views.account_page,
         name='account'),

    path('event/<str:pk>/', views.event_page,
         name='event'),
    path('project-submission/<str:pk>/', views.project_submission,
         name='project-submission'),
    path('registration_confirmation/<str:pk>/',
         views.registration_confirmation,
         name='registration_confirmation'),

]
