# Django Commands
dj-migrations:
	python manage.py makemigrations

dj-migrate:
	python manage.py migrate

dj-run:
	python manage.py runserver

dj-collect:
	python manage.py collectstatic

dj-superuser:
	python manage.py createsuperuser

dj-lint:
	djlint --indent=2 --reformat templates/

dj-dump:
	python manage.py dumpdata core.Address > data/address.json
	python manage.py dumpdata core.OpeningHour > data/openingHour.json
	python manage.py dumpdata core.SocialNetwork > data/socialNetwork.json
	python manage.py dumpdata core.Company > data/company.json
	python manage.py dumpdata core.About > data/about.json
	python manage.py dumpdata works.Achievement > data/achievements.json
	python manage.py dumpdata works.Position > data/positions.json
	python manage.py dumpdata works.Employee > data/employees.json
	python manage.py dumpdata works.Review > data/reviews.json
	python manage.py dumpdata works.Advantage > data/advantages.json
	python manage.py dumpdata works.Service > data/services.json

dj-upload:
	python manage.py upload_data

# Commands for working with a virtual environment
venv310:
	python3.10 -m venv .venv
	@echo "Virtual environment created for Python 3.10"

venv39:
	python3.9 -m venv .venv
	@echo "Virtual environment created for Python 3.9"


# Installing dependencies
install:
	poetry install

shell:
	poetry shell

# Linting and formatting
format:
	black .
	isort .

lint:
	flake8 .
	mypy .

# Running tests
test:
	pytest

# Full check (formatting, linting, tests)
check: format lint test


# Other utils

pre-deploy:
	mkdir cache_data
	mkdir logs
