from django.shortcuts import render
from datetime import datetime

def agenda_view(request):
    date = datetime.now().strftime("%Y-%m-%d")
    return render(request, 'agenda.html', {'date': date})

def notes_view(request):
    return render(request, 'notes.html')