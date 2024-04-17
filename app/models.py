from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatar/")
    message = models.ManyToManyField("Message")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From: {self.sender.username}, To: {self.receiver.username}, Content: {self.content}"