from django.contrib import admin
from .models import GameType, Court, Booking

admin.site.register(GameType)
admin.site.register(Court)
admin.site.register(Booking)
