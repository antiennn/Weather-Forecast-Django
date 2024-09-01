from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def send_custom_html_email(recipient_email,query):
    subject = 'Confirm Your Email Address'
    from_email = settings.DEFAULT_FROM_EMAIL
    to = recipient_email

    # Define the context for the template
    context = {
        'recipient_name': recipient_email,
        "query":query,
        'message': 'This is a custom HTML email sent from Django.',
    }

    # Render the HTML content using the template and context
    html_content = render_to_string('confirm_email.html', context)

    # Optionally, you can provide a plain text version of the email
    text_content = f"Hello {recipient_email},\n\nThis is a custom HTML email sent from Django."

    # Create the email object
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])

    # Attach the HTML version
    msg.attach_alternative(html_content, "text/html")

    # Send the email
    msg.send()


def send_weather_forecast_email(recipient_email,city,temperature,humidity,wind_speed,condition):
    subject = 'Weather forecast today'
    from_email = settings.DEFAULT_FROM_EMAIL
    to = recipient_email

    # Define the context for the template
    context = {
        'recipient_name': recipient_email,
        'city': city,
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "condition": condition
    }

    # Render the HTML content using the template and context
    html_content = render_to_string('weather_forecast_email.html', context)

    # Optionally, you can provide a plain text version of the email
    text_content = f"Hello {recipient_email},\n\nThis is a custom HTML email sent from Django."

    # Create the email object
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])

    # Attach the HTML version
    msg.attach_alternative(html_content, "text/html")

    # Send the email
    msg.send()
