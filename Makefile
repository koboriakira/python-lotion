.PHONY: test
test:
	@pipenv run pytest -m "not learning and not api"

.PHONY: test-current
test-current:
	@pipenv run pytest -m "current"


.PHONY: test-all
test-all:
	@pipenv run pytest
