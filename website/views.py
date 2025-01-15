from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'fullsite/home.html')

def events(request):
    return render(request, 'fullsite/events.html', {'title': 'Events'})

def booking(request):
    return render(request, 'fullsite/booking.html', {'title': 'Booking'})

def about(request):
    return render(request, 'fullsite/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'fullsite/contact.html', {'title': 'Contact'})