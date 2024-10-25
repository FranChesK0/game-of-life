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

.PHONY: debug
debug:
	python game-of-life/main.py --debug

.DEFAULT_GOAL := run
