.PHONY: install test run lint format docs docker-build docker-up docker-down

install:
	pip install -r requirements-dev.txt

test:
	pytest tests/ -v

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

lint:
	flake8 app tests

format:
	black app tests

docs:
	mkdocs serve

docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down
