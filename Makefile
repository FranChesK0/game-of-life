.PHONY: lint
lint:
	isort .
	black .
	flake8 .
	mypy .

.PHONY: pc
pc:
	pre-commit run --all-files
