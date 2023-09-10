test:
	pytest -svv --log-cli-level=INFO --cov=app/ tests/ --hypothesis-show-statistics

dev:
	pre-commit run -a
	mypy ../code_quality --check-untyped-defs
	pytype ../code_quality
	radon cc -a -nb ../code_quality
	pytest -svv --log-cli-level=INFO --cov=app/ tests/ --hypothesis-show-statistics
