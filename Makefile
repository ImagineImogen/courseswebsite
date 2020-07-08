RUN=docker-compose exec api
DJANGO_SETTINGS_MODULE=config.settings.docker

.PHONY: rebuild stop start restart manage

rebuild:
	docker-compose down && docker-compose up -d --build --remove-orphans

stop:
	docker-compose stop

start:
	docker-compose up -d --build --remove-orphans

restart:
	docker-compose stop && docker-compose up -d --build --remove-orphans

manage:
	$(RUN) python ./manage.py $(filter-out $@,$(MAKECMDGOALS)) --settings=$(DJANGO_SETTINGS_MODULE)