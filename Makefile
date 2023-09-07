test:
	pytest -svv --log-cli-level=INFO --cov=app/ tests/ --hypothesis-show-statistics

dev:
	pre-commit run -a
	mypy ../app --check-untyped-defs
	pytype ../app
	radon cc -a -nb ../app
	pytest -svv --log-cli-level=INFO --cov=app/ tests/ --hypothesis-show-statistics
