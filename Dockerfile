# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV API_WEATHER_FORECAST=***
ENV REDIS=***
ENV EMAIL_HOST_USER=***
ENV EMAIL_HOST_PASSWORD=***
ENV DB_PASSWORD=***
ENV DB_USER=***
ENV DB_HOST=***

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev && \
    apt-get clean

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the Django development server
CMD ["python", "./weatherforecast/manage.py", "runserver", "0.0.0.0:8000"]