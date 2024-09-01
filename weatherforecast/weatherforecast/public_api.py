import requests
from .settings import API_WEATHER_FORECAST


def get_weather_forecast(q, day, lang):
    return requests.get(
        f"http://api.weatherapi.com/v1/forecast.json?q={q}&days={day}&key={API_WEATHER_FORECAST}&lang={lang}").json()


def get_suggest_search(q):
    return requests.get(
        f"http://api.weatherapi.com/v1/search.json?q={q}&key={API_WEATHER_FORECAST}").json()
