from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    hackathon_participant = models.BooleanField(null=True,
                                                default=True)
    # avatar

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500,
                                   null=True, blank=True)
    participants = models.ManyToManyField(User,
                                          blank=True, related_name='events')
    date = models.DateTimeField()
    upadated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Submission(models.Model):
    participant = models.ForeignKey(User,
                                    on_delete=models.SET_NULL,
                                    null=True)
    events = models.ForeignKey(Event,
                               on_delete=models.SET_NULL,
                               null=True)
    details = models.TextField(max_length=500,
                               null=True, blank=True)

    def __str__(self) -> str:
        return str(self.events) + " --- " + str(self.participant)
