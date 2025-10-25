from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import LearningJourney, AboutMe

# View for the homepage
def index(request):
    journeys = LearningJourney.objects.all()
    return render(request, 'kJourney/index.html', {'journeys': journeys})

# View for the About Me page
def about_me(request):
    about = AboutMe.objects.first()
    return render(request, 'kJourney/aboutMe.html', {'about': about})

