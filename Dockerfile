FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=config.settings.docker
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential \
    libssl-dev libffi-dev python3-dev
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/