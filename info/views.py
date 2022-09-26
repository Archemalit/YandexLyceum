from django.shortcuts import render

def profile(request):
    context = {"city": "Уфа"}
    return render(request, 'info/profile.html', context)