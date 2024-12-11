.PHONY: test
test:
	@pipenv run pytest -m "not learning and not get_api and not post_api"

.PHONY: test-current
test-current:
	@pipenv run pytest -m "current"

.PHONY: test-get-api
test-get-api:
	@pipenv run pytest -m "get_api"

.PHONY: test-post-api
test-post-api:
	@pipenv run pytest -m "post_api"

.PHONY: test-all
test-all:
	@pipenv run pytest
