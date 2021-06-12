import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d63f87ad6257960fe20cf6b7d384a95'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()

    cities = City.objects.all()
    weather_data =[]
    try:
        for city in cities:
            r = requests.get(url.format(city))
            r_json = r.json()
            city_weather = {
            'city' : city.name,
            'temperature' : r_json['main']['temp'],
            'description' : r_json['weather'][0]['description'],
            'icon' : r_json['weather'][0]['icon']
            }

            weather_data.append(city_weather)
    except KeyError:
        pass
    except EXCEPTION as e:
        pass
    
    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather_app/weather.html', context)
