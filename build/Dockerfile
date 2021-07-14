FROM python:3.8



SHELL ["/bin/bash", "-c"]

RUN mkdir /app
WORKDIR /app

COPY api/ /app/

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y binutils
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libproj-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y gdal-bin

RUN pip install --upgrade pip \
&& pip install --no-cache-dir -r requirements/dev.txt

RUN ["pwd"]
RUN ["ls", "-l"]
CMD ["./manage.py","runserver", "0.0.0.0:8000"]