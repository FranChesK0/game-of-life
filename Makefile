.PHONY: lint
lint:
	isort .
	black .
	flake8 .
	mypy .

.PHONY: pc
pc:
	pre-commit run --all-files

.PHONY: run
run:
	python game-of-life/main.py

.DEFAULT_GOAL := run
