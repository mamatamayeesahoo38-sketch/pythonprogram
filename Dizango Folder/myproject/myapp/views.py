from django.shortcuts import render

def input_page(request):
    return render(request, 'input.html')


def output_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        hobby = request.POST.get('hobby')
        gender = request.POST.get('gender')
        country = request.POST.get('country')

        return render(request, 'output.html', {
            'name': name,
            'address': address,
            'hobby': hobby,
            'gender': gender,
            'country': country
        })
