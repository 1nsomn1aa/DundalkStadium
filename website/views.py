from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
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

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        topic = request.POST.get('topic')
        message = request.POST.get('message')

        subject = f'Contact Us Form Submission from {firstname}'
        body = f'You have received a new message from your contact form:\n\n' \
               f'First Name: {firstname}\n' \
               f'Last Name: {lastname}\n' \
               f'Email: {email}\n' \
               f'Topic: {topic}\n' \
               f'Message:\n{message}'

        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        messages.success(request, 'Your message has been sent successfully. We will get back to you soon!')

    return render(request, 'fullsite/contact.html', {'title': 'Contact'})

def news(request, post_id):
    selected_news = News.objects.get(id=post_id)
    recent_news = News.objects.order_by('-date_posted')[:3]

    context = {
        'news': selected_news,
        'recent_news': recent_news,
    }
    return render(request, 'fullsite/news.html', context)