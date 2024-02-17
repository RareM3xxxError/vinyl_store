# views.py in timenow app

from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def show_time_page(request):
    return render(request, 'timenow/current_time.html')

def current_time(request):
    now = datetime.now().strftime("%H:%M:%S")
    return JsonResponse({'time': now})