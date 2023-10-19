from api.adapters.outbound.logger.dev import get_logger_dev
from api.adapters.outbound.repository.memory.create_customer import (
    get_create_customer_repo_memory,
)
from api.adapters.outbound.repository.memory.create_order import (
    get_create_order_repo_memory,
)
from api.app_factory import app_factory
from api.core.ports.outbound.logger import get_logger
from api.core.ports.outbound.repository.create_customer import get_create_customer_repo
from api.core.ports.outbound.repository.create_order import (
    get_create_order_repo,
)
from api.settings.factory import settings_factory


settings = settings_factory()
app = app_factory(settings=settings)
app.dependency_overrides[get_logger] = get_logger_dev
app.dependency_overrides[get_create_order_repo] = get_create_order_repo_memory  # noqa: E501
app.dependency_overrides[get_create_customer_repo] = get_create_customer_repo_memory  # noqa: E501
