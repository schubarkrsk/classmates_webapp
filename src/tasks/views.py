from django.shortcuts import render
from .models import Tasks
from .models import Events
# Create your views here.

def index(request):
    tasks = Tasks.objects.all()
    event = Events.objects.all()
    return render(request, 'tasks_events/tasks_events.html', {'tasks': tasks, 'event': event})