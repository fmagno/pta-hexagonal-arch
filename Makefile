

#--- SETUP --------------------------------#
include config.mk

export

SHELL := /bin/bash

VENV?=.venv
PYTHON=${VENV}/bin/python3
PIP=${VENV}/bin/pip
BUILD_DIR=build


$(VENV): ## Create virtualenv and install pip-tools
	python3 -m venv $(VENV)
	${PIP} install -U pip
	${PIP} install pip-tools wheel

install: $(VENV) requirements.txt ## Sync virtual environment with dependencies
	$(VENV)/bin/pip-sync

install-dev: $(VENV) requirements-dev.txt ## Create development environment
	$(VENV)/bin/pip-sync requirements-dev.txt
	$(VENV)/bin/pre-commit install

requirements.txt: pyproject.toml
	$(VENV)/bin/pip-compile -o requirements.txt pyproject.toml

requirements-dev.txt: pyproject.toml
	$(VENV)/bin/pip-compile -o requirements-dev.txt --extra dev pyproject.toml



.PHONY: format
format:
	isort api/
	black api/



#--- RUN APP --------------------------------#

.PHONY: run-dev
run-dev: requirements-dev.txt
	CONTROLLER_PORT=$(CONTROLLER_PORT)		#TODO: * error decoding 'ports': Invalid containerPort: 9000 \
	DEBUG_PORT=$(DEBUG_PORT) 				#TODO: * error decoding 'ports': Invalid containerPort: 4567 \
		docker compose -f infra/docker/docker-compose.local-dev.yml build

	CONTROLLER_PORT=$(CONTROLLER_PORT)		#TODO: \
	DEBUG_PORT=$(DEBUG_PORT)				#TODO: \
		docker compose -f infra/docker/docker-compose.local-dev.yml up

.PHONY: run-dev-debug
run-dev-debug: requirements-dev.txt
	CONTROLLER_PORT=$(CONTROLLER_PORT)		#TODO: * error decoding 'ports': Invalid containerPort: 9000 \
	DEBUG_PORT=$(DEBUG_PORT) 				#TODO: * error decoding 'ports': Invalid containerPort: 4567 \
	DEBUG_ENABLED=true \
		docker compose -f infra/docker/docker-compose.local-dev.yml build

	CONTROLLER_PORT=$(CONTROLLER_PORT)		#TODO: \
	DEBUG_PORT=$(DEBUG_PORT)				#TODO: \
	DEBUG_ENABLED=true \
		docker compose -f infra/docker/docker-compose.local-dev.yml up



.PHONY: stop-dev
stop-dev:
	CONTROLLER_PORT=$(CONTROLLER_PORT)		#TODO: \
	DEBUG_PORT=$(DEBUG_PORT)				#TODO: \
		docker compose -f infra/docker/docker-compose.local-dev.yml down || true


#--- TEST --------------------------------#



# run-test: stop clean
.PHONY: run-test
run-test: requirements-dev.txt
	CONTROLLER_PORT=$(CONTROLLER_PORT)		#TODO: * error decoding 'ports': Invalid containerPort: 9000 \
	DEBUG_PORT=$(DEBUG_PORT_TEST) 			#TODO: * error decoding 'ports': Invalid containerPort: 4567 \
		docker compose -f infra/docker/docker-compose.local-test.yml build

	CONTROLLER_PORT=$(CONTROLLER_PORT)		#TODO: \
	DEBUG_PORT=$(DEBUG_PORT_TEST)			#TODO: \
		docker compose -f infra/docker/docker-compose.local-test.yml up

.PHONY: run-test-debug
run-test-debug: requirements-dev.txt
	CONTROLLER_PORT=$(CONTROLLER_PORT)		#TODO: * error decoding 'ports': Invalid containerPort: 9000 \
	DEBUG_PORT=$(DEBUG_PORT_TEST) 			#TODO: * error decoding 'ports': Invalid containerPort: 4567 \
	DEBUG_ENABLED=true \
		docker compose -f infra/docker/docker-compose.local-test.yml build

	CONTROLLER_PORT=$(CONTROLLER_PORT)		#TODO: \
	DEBUG_PORT=$(DEBUG_PORT_TEST)			#TODO: \
	DEBUG_ENABLED=true \
		docker compose -f infra/docker/docker-compose.local-test.yml up


.PHONY: run-test-stop
run-test-stop: run-test stop-test



.PHONY: stop-test
stop-test:
	CONTROLLER_PORT=$(CONTROLLER_PORT)		#TODO: \
	DEBUG_PORT_TEST=$(DEBUG_PORT_TEST)		#TODO: \
		docker compose -f infra/docker/docker-compose.local-test.yml down || true


#--- TEARDOWN -----------------------------#

.PHONY: stop
stop: stop-dev stop-test


.PHONY: clean
clean: clean-files clean-volumes

.PHONY: clean-files
clean-files:
	find . \( -name __pycache__ -o -name "*.pyc" -o -name .pytest_cache -o -name .mypy_cache \) -exec rm -rf {} +

.PHONY: clean-volumes
clean-volumes:
	docker volume rm -f docker_local_postgres_data docker_local_test_postgres_data
	docker volume rm -f docker_prod_postgres_data docker_prod_test_postgres_data
