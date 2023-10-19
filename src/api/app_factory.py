from fastapi import FastAPI
from api.settings.pydantic import Settings
from fastapi.middleware.cors import CORSMiddleware
from api.controller.routes import router


def app_factory(settings: Settings):
    app = FastAPI(
        title=settings.APP_NAME,
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        # middleware=middleware,
    )

    if settings.CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[
                str(origin)
                for origin in settings.CORS_ORIGINS
                #
            ],
            # allow_origins=[
            #     "*",
            #     "http://api",
            # ],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    app.include_router(
        router=router,
        prefix=settings.API_URL_PREFIX,
    )

    return app
