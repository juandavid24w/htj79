# Pull base image
FROM python:3.11-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

COPY . .

RUN apt update -y
RUN apt upgrade -y
RUN apt install -y build-essential python3-dev python3-gdal nano vim curl

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN python3 manage.py collectstatic

CMD bash entrypoint.sh

#CMD gunicorn django_project.wsgi -w 3
