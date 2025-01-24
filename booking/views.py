from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import GameType, Booking, Court
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

@login_required
def booking_view(request):
    game_types = GameType.objects.all()
    courts = Court.objects.all()
    hours_range = list(range(10, 22))

    booked_slots = []
    available_slots = []

    selected_court = None
    selected_court_name = ""
    selected_date = None
    game_type = None
    is_checked = False

    if request.method == 'POST':
        game_type = request.POST.get('game-type')
        selected_court = request.POST.get('court')
        selected_date = request.POST.get('date')
        selected_time_slot = request.POST.get('time-slot')

        try:
            selected_court = int(selected_court)
            court = Court.objects.get(id=selected_court)
            selected_court_name = court.name
            is_checked = True
        except (ValueError, TypeError):
            return render(request, 'booking/booking.html', {
                'message': 'Invalid court selection. Please try again.',
                'game_types': game_types,
                'courts': courts,
                'available_slots': available_slots,
                'booked_slots': booked_slots,
                'hours_range': hours_range,
            })

        booked_slots = Booking.objects.filter(court_id=selected_court, date=selected_date).values_list('time_slot', flat=True)
        booked_slots = [slot.strftime('%H:%M') for slot in booked_slots]

        available_slots = [f"{hour}:00" for hour in hours_range if f"{hour}:00" not in booked_slots]

        if selected_time_slot:
            try:
                court = Court.objects.get(id=selected_court)
                booking = Booking(court=court, date=selected_date, time_slot=selected_time_slot, user=request.user)
                booking.save()

                messages.success(request, 'Booking successful!')
        
                send_mail(
                    'Booking Confirmation',
                    f'Hello {request.user.username},\n\n'
                    f'Your booking for {court.name} on {selected_date} at {selected_time_slot} has been confirmed!\n\n'
                    'Thank you for using our service!',
                    settings.EMAIL_HOST_USER,
                    [request.user.email],
                    fail_silently=False,
                )

                return redirect('profile')

            except Court.DoesNotExist:
                return render(request, 'booking/booking.html', {
                    'message': 'Selected court does not exist.',
                    'game_types': game_types,
                    'courts': courts,
                    'available_slots': available_slots,
                    'booked_slots': booked_slots,
                    'hours_range': hours_range,
                })

    return render(request, 'booking/booking.html', {
        'game_types': game_types,
        'courts': courts,
        'hours_range': hours_range,
        'booked_slots': booked_slots,
        'available_slots': available_slots,
        'game_type': game_type,
        'selected_court': selected_court,
        'selected_court_name': selected_court_name,
        'selected_date': selected_date,
        'is_checked': is_checked
    })