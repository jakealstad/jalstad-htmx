# jalstad-htmx
very simple django + htmx test

# development
* install docker
* create `local.py` in the `api` directory and include the following
	* `SECRET_KEY = '123'`
	* `DEBUG = True`
* run `./scripts/start_docker.sh`

## editor notes
* this project uses [ruff](https://github.com/astral-sh/ruff) for code linting and formatting
	* [configure your editor or ide](https://docs.astral.sh/ruff/editors/setup/) to run `ruff format` and `ruff check --fix` on save or use the [pre-commit](https://github.com/astral-sh/ruff-pre-commit)