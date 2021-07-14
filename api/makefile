build_dev:
	docker-compose --env-file ../build/env.dev -f ../build/docker-compose-dev.yml -p geofencing up -d --build --remove-orphans

build_prod:
	docker-compose --env-file ../build/env.prod -f ../build/docker-compose.yml -p geofencing up -d --build --remove-orphans
	
container:
	docker exec -it GeoFence bash

test:
	DJANGO_SETTINGS_MODULE=geoFencing.settings.test_settings pytest -v geoFencing/apps/geofence/tests.py

shell:
	./manage.py shell
run:
	./manage.py runserver 0:8000

makemigrations:
	./manage.py makemigrations

migrate:
	./manage.py migrate

createsuperuser:
	./manage.py createsuperuser

req-compile:
	@for fl in $(shell ls requirements/); do pip-compile requirements/$${fl}; done