from django.shortcuts import render, get_object_or_404
from .models import Room

# Create your views here.


def homepage(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get_or_404(Room, pk=pk)
    context = {
        'room': room
    }
    return render(request, 'base/room.html', context)
