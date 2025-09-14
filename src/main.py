# from fastapi import FastAPI
# from contextlib import asynccontextmanager
# from src.db.database import create_db_and_tables

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     create_db_and_tables()
#     yield

# app = FastAPI(
#     title="gis-api API",
#     description="API for gis-api",
#     version="0.1.0",
#     debug=True,
#     lifespan=lifespan
# )
from fastapi import FastAPI
from src.controller import region_controller

app = FastAPI(title="My API")

app.include_router(region_controller.router)