from django.urls import path
from . import views

urlpatterns = [

    # Auth URLs
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('event/<int:event_id>/apply/', views.event_apply_form, name='apply-form'),

    # Participant URLs
    path('participant/<int:participant_id>/profile/', views.participant_profile, name='participant-profile'),
    path('participant/<int:participant_id>/detail/', views.participant_detail, name='participant-detail'),

    # Main Pages
    path('', views.event_list, name='home'),  # Home page = event list
    path('events/', views.event_list, name='event-list'),
    path('event-detail/<int:event_id>/', views.event_detail, name='event-detail'),

    # Other Lists
    path('categories/', views.category_list, name='category-list'),
    path('attendees/', views.attendee_list, name='attendee-list'),
    path('tickets/', views.ticket_list, name='ticket-list'),
]
