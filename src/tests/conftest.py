import pytest
from api.adapters.outbound.logger.dev import logger_dev_factory
from api.adapters.outbound.repository.memory.create_customer import (
    create_customer_repo_memory_fct,
)
from api.adapters.outbound.repository.memory.create_order import (
    create_order_repo_memory_fct,
)

from api.settings.factory import settings_factory


@pytest.fixture
async def settings():
    settings = settings_factory(
        APP_NAME="test_app",
        CONTROLLER_APP="fastapi",
        CONTROLLER_HOST="0.0.0.0",
        CONTROLLER_PORT=9000,
        REPOSITORY="memory",
        CORS_ORIGINS="*",
        API_URL_PREFIX="/api",
        API_APP="api:app",
        DEBUG_HOST="0.0.0.0",
        DEBUG_PORT=5678,
    )
    return settings


@pytest.fixture
async def logger_dev(settings):
    logger = await logger_dev_factory(settings=settings)
    return logger


@pytest.fixture
async def create_customer_repo_memory(
    settings,
    logger_dev,
):
    create_customer_repo_memory = await create_customer_repo_memory_fct(
        settings=settings,
        logger=logger_dev,
    )
    return create_customer_repo_memory


@pytest.fixture
async def create_first_order_repo_memory(
    settings,
    logger_dev,
):
    create_first_order_repo_memory = await create_order_repo_memory_fct(
        settings=settings,
        logger=logger_dev,
    )
    return create_first_order_repo_memory
