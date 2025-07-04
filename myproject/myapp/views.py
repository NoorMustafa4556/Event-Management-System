from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q

from .models import Event, Attendee, Category, Ticket, Participant

# ----------------------------
# 🔐 AUTHENTICATION VIEWS
# ----------------------------

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')
            
    return render(request, 'events/user_side/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password!')

    return render(request, 'events/user_side/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# ----------------------------
# 📅 EVENT VIEWS
# ----------------------------

def event_list(request):
    query = request.GET.get('q')
    events = Event.objects.all()

    if query:
        events = events.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query)
        )

    # Restrict data shown to unauthenticated users
    if not request.user.is_authenticated:
        for event in events:
            event.description = None
            event.location = None
            event.category = None
            event.date = None

    return render(request, 'events/event_list.html', {'events': events})


@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    participants = Participant.objects.filter(event=event, is_selected=True)
    return render(request, 'events/event_detail.html', {
        'event': event,
        'participants': participants
    })


@login_required
def event_apply_form(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        reason = request.POST.get('reason')
        skills = request.POST.get('skills')
        experience = request.POST.get('experience')
        achievements = request.POST.get('achievements')

        if Participant.objects.filter(event=event, email=email).exists():
            messages.warning(request, "You have already applied. Please wait for approval.")
        else:
            Participant.objects.create(
                event=event,
                name=name,
                email=email,
                reason_to_join=reason,
                skills=skills,
                experience=experience,
                achievements=achievements,
            )
            messages.success(request, "Application submitted successfully!")

        return HttpResponseRedirect(reverse('event-detail', args=[event.id]))

    already_applied = Participant.objects.filter(event=event, email=request.user.email).exists()
    return render(request, 'events/apply_form.html', {
        'event': event,
        'already_applied': already_applied
    })


# ----------------------------
# 👤 PARTICIPANT VIEWS
# ----------------------------

@login_required
def participant_detail(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    total_events = Participant.objects.filter(email=participant.email, is_selected=True).count()

    return render(request, 'events/participant_detail.html', {
        'participant': participant,
        'total_events': total_events
    })


@login_required
def participant_profile(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    return render(request, 'events/participant_profile.html', {'participant': participant})


# ----------------------------
# 📂 MISC LIST VIEWS
# ----------------------------

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'events/category_list.html', {'categories': categories})


@login_required
def attendee_list(request):
    attendees = Attendee.objects.all()
    return render(request, 'events/attendee_list.html', {'attendees': attendees})


@login_required
def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'events/ticket_list.html', {'tickets': tickets})
