from django.shortcuts import render
from .models import Person

def input_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        hobby = request.POST.get('hobby')
        gender = request.POST.get('gender')
        country = request.POST.get('country')

        # Save to database
        Person.objects.create(
            name=name,
            address=address,
            hobby=hobby,
            gender=gender,
            country=country
        )

    return render(request, 'input.html')


def output_page(request):
    persons = Person.objects.all()
    return render(request, 'output.html', {'persons': persons})
def show_records(request):
    persons = Person.objects.all()   # Get all records
    return render(request, 'output.html', {'persons': persons})