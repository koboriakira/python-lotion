.PHONY: test
test:
	@pipenv run pytest -m "not slow and not learning and not use_genuine_api"

.PHONY: test-all
test-all:
	@pipenv run pytest
