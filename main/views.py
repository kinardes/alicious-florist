from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245642',
        'name': 'Alica Kinar Deska',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
