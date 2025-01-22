from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Court, Bookings

@login_required
def book_area(request):
    if request.method == 'POST':
        court_id = request.POST['court_id']
        booking_time = request.POST['booking_time']
        user_name = request.POST['user_name']

        new_booking = Bookings.objects.create(
            court_id=court_id,
            booking_time=booking_time,
            user_name=user_name
        )
        new_booking.save()

    courts = Court.objects.all()
    return render(request, 'bookings/booking.html', {'courts': courts})