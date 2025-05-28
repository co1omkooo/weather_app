import requests

from django.http import JsonResponse
from django.shortcuts import render

from .forms import CityForm


def get_weather_data(city):
    # Шаг 1: Получение координат по названию города
    geocode_url = (
        f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    )
    geo_response = requests.get(geocode_url).json()

    if "results" not in geo_response:
        return None

    location = geo_response["results"][0]
    latitude = location["latitude"]
    longitude = location["longitude"]

    # Шаг 2: Получение прогноза погоды
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&hourly=temperature_2m,precipitation"
        f"&forecast_days=1"
        f"&timezone=auto"
    )
    weather_response = requests.get(weather_url).json()
    hourly = weather_response.get("hourly", {})
    forecast = []
    for i in range(len(hourly["time"])):
        forecast.append({
            "time": hourly["time"][i],
            "temperature": hourly["temperature_2m"][i],
            "precipitation": hourly["precipitation"][i],
        })
    return {
        "city": city,
        "latitude": latitude,
        "longitude": longitude,
        "forecast": forecast
    }


def index(request):
    weather_data = None
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]
            weather_data = get_weather_data(city)
    else:
        form = CityForm()

    return render(request, "weather/index.html", {
        "form": form,
        "weather_data": weather_data
    })


def autocomplete(request):
    query = request.GET.get("term", "")
    if not query:
        return JsonResponse([], safe=False)

    try:
        url = (
            f"https://geocoding-api.open-meteo.com/v1/search?name={query}&count=5"
        )
        response = requests.get(url, timeout=5)
        data = response.json()

        results = []
        for item in data.get("results", []):
            label = f"{item['name']}, {item.get('country', '')}"
            results.append(label)

        return JsonResponse(results, safe=False)

    except Exception as e:
        print("Autocomplete error:", e)
        return JsonResponse([], safe=False)
