.PHONY: lint
lint:
	isort .
	black .
	flake .
	mypy .

.PHONY: pc
pc:
	pre-commit run --all-files
