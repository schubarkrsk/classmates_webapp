from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from .forms import MessageForm

@login_required
def chat(request, username):
    sender = request.user
    receiver = User.objects.get(username=username)
    messages = Message.objects.filter(sender=sender, receiver=receiver) | Message.objects.filter(sender=receiver, receiver=sender)
    messages = messages.order_by('timestamp')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.receiver = receiver
            message.save()
            return redirect('chat', username=username)
    else:
        form = MessageForm()
    return render(request, 'chat.html', {'form': form, 'messages': messages, 'receiver': receiver})
