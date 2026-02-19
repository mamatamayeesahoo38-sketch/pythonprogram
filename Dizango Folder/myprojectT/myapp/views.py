from django.shortcuts import render
from .models import Person

def show_records(request):
    persons = Person.objects.all()   # Get all records
    return render(request, 'output.html', {'persons': persons})
