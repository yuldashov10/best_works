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
