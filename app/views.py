from django.shortcuts import render, get_object_or_404
from .models import *

def home(request):
    users = User.objects.all()
    messages = {}

    for user in users:
        sender_messages = Message.objects.filter(sender=user).order_by('-timestamp')
        receiver_messages = Message.objects.filter(receiver=user).order_by('-timestamp')
        
        all_messages = list(sender_messages) + list(receiver_messages)
        all_messages.sort(key=lambda x: x.timestamp, reverse=True)
        
        messages[user] = all_messages
    
    return render(request, "base.html", {"users": users, "messages": messages})

def detail(request, pk):
    user = get_object_or_404(User, id=pk)
    users = User.objects.all()


    data = {
        "user" : user,
        "users" : users
    }
    return render(request, "detail.html", data)