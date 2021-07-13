build_dev:
	docker-compose -f ../build/docker-compose.yml -p geofencing up -d --build --remove-orphans

container:
	docker exec -it GeoFence bash

test:
	DJANGO_SETTINGS_MODULE=settings.test_settings pytest -v service_area/tests

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