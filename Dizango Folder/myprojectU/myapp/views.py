from django.shortcuts import render, redirect
from .models import Student

# CREATE
def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        Student.objects.create(name=name, address=address)
        return redirect('show')
    return render(request, 'add.html')

# READ
def show_students(request):
    students = Student.objects.all()
    return render(request, 'show.html', {'students': students})

# UPDATE
def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.name = request.POST['name']
        student.address = request.POST['address']
        student.save()
        return redirect('show')
    return render(request, 'update.html', {'student': student})

# DELETE
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('show')
