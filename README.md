## Development Notes

### Running this API in development mode

- Connect to the TACC VPN
- Configure a `dev.env` file. This file will be ignored by git.
- `docker-compose -f docker-compose.dev.yml up`
- Browse to `http://localhost:8000/docs`, or `curl` any of the endpoints, e.g. `curl http://localhost:8000/topics`

### Running Unit Tests Locally

- Make sure you have Python `poetry` installed.
- Install the project dependencies locally with `poetry install`.
- Run unit tests with `poetry run pytest`

### Running the code formatter

- Make sure you have poetry dependencies installed locally
- Run code formatting with `poetry run black democratizing`