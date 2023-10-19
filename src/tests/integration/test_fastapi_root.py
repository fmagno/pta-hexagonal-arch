from fastapi.testclient import TestClient
import pytest

from api.app import app_factory

pytestmark = pytest.mark.asyncio


@pytest.mark.smoke
@pytest.mark.debug
@pytest.mark.integration
async def test_root_endpoint(settings):
    app = app_factory(settings=settings)
    client = TestClient(app)
    response = client.get("/")

    assert response.status_code == 200
