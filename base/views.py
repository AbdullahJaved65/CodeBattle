from django.shortcuts import render
from .models import User, Event, Submission


def home_page(request):
    users = User.object.filter(hackathon_participant= True)
    
    return render(request, 'home.html')
