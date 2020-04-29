from django.shortcuts import render
from .models import service

def services(request):
    services = service.objects.all()
    return render(request, 'services/services.html', {'services':services})
