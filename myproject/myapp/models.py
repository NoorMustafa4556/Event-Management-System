from django.db import models
from django.contrib.auth.models import User

# ✅ Category Model (moved to top)
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# ✅ Event Model
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField()  # renamed for clarity
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

# ✅ Participant Model
class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    reason_to_join = models.TextField()
    skills = models.TextField()
    experience = models.TextField(blank=True, null=True)
    achievements = models.TextField(blank=True, null=True)
    is_selected = models.BooleanField(default=False)  # <-- YEH BOHOT ZARURI HAI

    def __str__(self):
        return self.name

# ✅ Attendee Model
class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} attending {self.event.title}"

# ✅ UserProfile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username

# ✅ Ticket Model
class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    sold = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.event.title} - Rs.{self.price} ({self.sold}/{self.quantity} sold)"
