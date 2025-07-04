from django.contrib import admin
from .models import Category, Event, Attendee, UserProfile, Ticket

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date_time')
    list_filter = ('date_time',)
    search_fields = ['title', 'description', 'location']

@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'event', 'registered_at']
    list_filter = ['event', 'registered_at']
    search_fields = ['user__username', 'event__title']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone', 'address']

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'price', 'quantity', 'sold']
    list_filter = ['event']
    search_fields = ['event__title']

from .models import Participant

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'event', 'is_selected']
    list_editable = ['is_selected']
    list_filter = ['is_selected', 'event']
    search_fields = ['name', 'email']
