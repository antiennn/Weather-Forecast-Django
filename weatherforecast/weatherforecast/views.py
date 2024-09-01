from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets

from .utils import *
from .models import Subscribe
from .public_api import get_suggest_search, get_weather_forecast


class WeatherForecastViewSet(viewsets.ViewSet):
    @action(methods=['GET'], detail=False, url_path='search')
    def search(self, request):
        try:
            query = request.query_params.get('q')
            return Response(data=get_suggest_search(query), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=False, url_path='forecast')
    def forecast(self, request):
        try:
            query = request.query_params.get('q')
            days = request.query_params.get('days')
            lang = request.query_params.get('lang')
            # get cache
            cache_key = f'weather_{query}_{days}_{lang}'
            cached_response = cache.get(cache_key)
            # check cache exist
            if cached_response:
                return Response(data=cached_response, status=status.HTTP_200_OK)
            # get data from api
            data = get_weather_forecast(query, days, lang)
            # set cache 5 minutes
            cache.set(cache_key, data, timeout=60 * 5)
            # return client
            return Response(data=data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=False, url_path='sendmail')
    def sendmail(self, request):
        try:
            email = request.data.get('email')
            query = request.data.get('query')
            send_custom_html_email(email, query)
            return Response(data={"please check your email to confirm"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=False, url_path='confirm')
    def confirm(self, request):
        try:
            email = request.query_params.get('email')
            query = request.query_params.get('query')
            list_sub = Subscribe.objects.filter(email=email,query=query)
            if len(list_sub) == 0:
                temp_sub = Subscribe.objects.create(email=email, query=query)
                return render(request, 'success.html')
            return Response(data="not found email", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=False, url_path='unsubscribe')
    def unsubscribe(self, request):
        try:
            email = request.query_params.get('email')
            Subscribe.objects.filter(email=email).delete()
            return render(request, 'unsubscribe.html')
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)



