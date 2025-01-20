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

def news(request, post_id):
    selected_news = News.objects.get(id=post_id)
    recent_news = News.objects.order_by('-date_posted')[:3]

    context = {
        'news': selected_news,
        'recent_news': recent_news,
    }
    return render(request, 'fullsite/news.html', context)