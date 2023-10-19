# from fastapi import FastAPI

# from api.settings.pydantic import Settings
# from backup.controller import Controller
# from fastapi.middleware.cors import CORSMiddleware
# from .routes import router


# class FastapiController(Controller):
#     def __init__(
#         self,
#         settings: Settings,
#     ):
#         self.settings = settings

#         self.app = FastAPI(
#             title=settings.APP_NAME,
#             docs_url="/api/docs",
#             redoc_url="/api/redoc",
#             openapi_url="/api/openapi.json",
#             # middleware=middleware,
#         )

#         if settings.CORS_ORIGINS:
#             self.app.add_middleware(
#                 CORSMiddleware,
#                 allow_origins=[
#                     str(origin)
#                     for origin in settings.CORS_ORIGINS
#                     #
#                 ],
#                 # allow_origins=[
#                 #     "*",
#                 #     "http://api",
#                 # ],
#                 allow_credentials=True,
#                 allow_methods=["*"],
#                 allow_headers=["*"],
#             )

#         @self.app.get("/")
#         def read_root():
#             return {"Hello": "World"}

#         self.app.include_router(
#             router=router,
#             prefix=self.settings.API_URL_PREFIX,
#         )

#     # def run(self):
#     #     print("fastapi app launched...")
#     #     print(f"controller host: {self.settings.CONTROLLER_HOST}")
#     #     print(f"controller port: {self.settings.CONTROLLER_PORT}")
#     #     uvicorn.run(
#     #         self.app,
#     #         host=self.settings.CONTROLLER_HOST,
#     #         port=self.settings.CONTROLLER_PORT,
#     #     )

#     def get_app(self):
#         return self.app
