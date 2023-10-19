# pizza tycoon web app configuration

# Build
BUILDKIT_PROGRESS = plain

# App
APP_NAME = pta
CONTROLLER_APP = fastapi
CONTROLLER_HOST = 0.0.0.0
CONTROLLER_PORT = 9000
REPOSITORY = memory
CORS_ORIGINS = *
API_URL_PREFIX = /api
API_APP = api.app:app

# pydebug - on/off
DEBUG_ENABLED = false

# debug - app
DEBUG_HOST = 0.0.0.0
DEBUG_PORT = 5678

# debug - tests
DEBUG_HOST_TEST = 0.0.0.0
DEBUG_PORT_TEST = 5679

# uvicorn
UVICORN_WORKERS = 1
