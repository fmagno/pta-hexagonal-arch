# from config import Settings


from functools import lru_cache
from api.settings.pydantic import Settings


def settings_factory(*args, **kwargs):
    settings = Settings(*args, **kwargs)

    print(settings)
    return settings


@lru_cache()
def get_settings():
    settings = settings_factory()
    return settings
