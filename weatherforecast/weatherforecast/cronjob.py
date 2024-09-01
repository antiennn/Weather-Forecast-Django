from .models import Subscribe
from .public_api import get_weather_forecast
from .utils import send_weather_forecast_email


def sendweatherforecastemail():
    for subscribe in Subscribe.objects.all():
        data = get_weather_forecast(subscribe.query, 1, "en")
        send_weather_forecast_email(subscribe.email,
                                    data.get("location").get("name"),
                                    data.get("current").get("temp_c"),
                                    data.get("current").get("humidity"),
                                    data.get("current").get("wind_mph"),
                                    data.get("current").get("condition").get("text"))
