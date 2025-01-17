from django.shortcuts import render
from .models import News

def home(request):
    context = {
        'news': News.objects.all()
    }
    return render(request, 'fullsite/home.html', context)

def events(request):
    return render(request, 'fullsite/events.html', {'title': 'Events'})

def booking(request):
    return render(request, 'fullsite/booking.html', {'title': 'Booking'})

def about(request):
    return render(request, 'fullsite/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'fullsite/contact.html', {'title': 'Contact'})