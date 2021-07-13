FROM python:3.8

ENV PYTHONUNBUFFERED 1

ENV DJANGO_SETTINGS_MODULE=geoFencing.settings.dev_settings
ENV DJANGO_SECRET="dsnjkcdslcndscjkejerbjrebgerhgberincdsnc21e1232"
ENV DB_HOST=db
ENV TEST_DB=testdb
ENV POSTGRES_DB=app
ENV POSTGRES_USER=postgres_user
ENV POSTGRES_PASSWORD=supersecretpassword

SHELL ["/bin/bash", "-c"]

RUN mkdir /app
WORKDIR /app

COPY api/ /app/

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y binutils
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libproj-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y gdal-bin

RUN pip install --upgrade pip \
&& pip install --no-cache-dir -r requirements/dev.txt

CMD  ["tail", "-f", "/dev/null"]