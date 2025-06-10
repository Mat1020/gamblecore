from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def terminal_view(request):
    return render(request, "game/terminal.html")