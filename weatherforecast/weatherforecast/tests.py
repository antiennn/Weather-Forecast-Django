from django.test import TestCase, Client


class WeatherForecastTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_forecast(self):
        # HaNoi capital
        q = "hanoi"
        # number of days
        day = 4
        # language
        language = "vi"
        response = self.client.get(f'/api/forecast/?q={q}&days={day}&lang={language}')
        self.assertEqual(response.status_code, 200)

    def test_get_suggest(self):
        # HaNoi capital
        q = "saigon"
        response = self.client.get(f'/api/search/?q={q}')
        self.assertEqual(response.status_code, 200)
