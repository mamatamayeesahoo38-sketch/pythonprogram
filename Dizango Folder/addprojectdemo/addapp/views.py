from django.shortcuts import render

def input_page(request):
    return render(request, 'addapp/input.html')

def result_page(request):
    if request.method == 'POST':
        n1 = int(request.POST['num1'])
        n2 = int(request.POST['num2'])
        res = n1 + n2
        return render(request, 'addapp/result.html', {'result': res})
