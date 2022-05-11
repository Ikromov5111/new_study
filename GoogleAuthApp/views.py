from django.shortcuts import render

# def view_name(request):
#     return render(request, 'authapp/index.html')

# Create your views here.
def view_name(request):
    return render(request, 'authapp\index.html', {})
