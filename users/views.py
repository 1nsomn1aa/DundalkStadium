from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from booking.models import Booking

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username {username} is already taken.')
                return render(request, 'users/register.html', {'form': form})

            user = form.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        try:
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        except Profile.DoesNotExist:
            p_form = ProfileUpdateForm(request.POST, request.FILES)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Successfully updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        try:
            p_form = ProfileUpdateForm(instance=request.user.profile)
        except Profile.DoesNotExist:
            p_form = ProfileUpdateForm()

    user_bookings = Booking.objects.filter(user=request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Profile',
        'user': request.user,
        'user_bookings': user_bookings, 
    }

    return render(request, 'users/profile.html', context)

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    messages.success(request, 'Booking deleted successfully.')
    return redirect('profile')