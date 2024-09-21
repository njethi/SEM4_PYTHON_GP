from django.shortcuts import render
from .models import Weather
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    weather = Weather.objects.all()
    return render(request,'home.html',{'weather':weather})
def detail(request, weather_id):
    weather = get_object_or_404(Weather,pk=weather_id)
    return render(request, 'detail.html',{'weather':weather})