from fastapi.testclient import TestClient
import pytest

from api.adapters.outbound.logger.dev import get_logger_dev
from api.adapters.outbound.repository.memory.create_customer import (
    get_create_customer_repo_memory,
)
from api.adapters.outbound.repository.memory.create_order import (
    get_create_order_repo_memory,
)
from api.app_factory import app_factory

# from api.controller.first_order.dtos import CreateFirstOrderCreateDto
from api.core.ports.outbound.logger import get_logger
from api.core.ports.outbound.repository.create_customer import get_create_customer_repo
from api.core.ports.outbound.repository.create_order import (
    get_create_order_repo,
)


pytestmark = pytest.mark.asyncio


@pytest.fixture
async def marge_first_order_json():
    return {"customer": {"name": "Marge"}}


@pytest.mark.integration
@pytest.mark.first_order
# @pytest.mark.skip
async def test_first_order_creation_with_valid_payload_int(
    settings,
    marge_first_order_json,
):
    """
    Integration: Should create a first order successfully with a valid payload.
    """

    app = app_factory(settings=settings)
    app.dependency_overrides[get_logger] = get_logger_dev
    app.dependency_overrides[get_create_order_repo] = get_create_order_repo_memory  # noqa: E501
    app.dependency_overrides[get_create_customer_repo] = get_create_customer_repo_memory  # noqa: E501

    client = TestClient(app)
    response = client.post("/api/first-order", json=marge_first_order_json)

    assert response.status_code == 200


# def test_create_first_order(settings):
