from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306230685',
        'name': 'Naya Kusumahayati Rachmi',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)

# Create your views here.
